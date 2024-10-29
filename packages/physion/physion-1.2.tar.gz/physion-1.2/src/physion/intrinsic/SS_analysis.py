import sys, os, shutil, glob, time, subprocess, pathlib, json, tempfile, datetime
import numpy as np
import pynwb, PIL, pandas
from PyQt5 import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
import matplotlib.pylab as plt
from scipy.interpolate import interp1d

from physion.utils.paths import FOLDERS, python_path
from physion.utils.files import last_datafolder_in_dayfolder, day_folder
from physion.intrinsic.tools import default_segmentation_params
from physion.intrinsic import tools as intrinsic_analysis

power_color_map = pg.ColorMap(pos=np.linspace(0.0, 1.0, 3),
                              color=[(0, 0, 0),
                                     (100, 100, 100),
                                     (255, 200, 200)]).getLookupTable(0.0, 1.0, 256)

signal_color_map = pg.ColorMap(pos=np.linspace(0.0, 1.0, 3),
                               color=[(0, 0, 0),
                                      (100, 100, 100),
                                      (255, 255, 255)]).getLookupTable(0.0, 1.0, 256)

def gui(self,
        box_width=250,
        tab_id=2):

    self.windows[tab_id] = 'ISI_analysis'

    tab = self.tabs[tab_id]

    self.cleanup_tab(tab)
    
    self.datafolder, self.IMAGES = '', {} 
    self.subject, self.timestamps, self.data = '', '', None


    ##########################################################
    ####### GUI settings
    ##########################################################

    # ========================================================
    #------------------- SIDE PANELS FIRST -------------------
    self.add_side_widget(tab.layout, 
            QtWidgets.QLabel('     _-* INTRINSIC IMAGING MAPS *-_ '))
    # folder box
    self.add_side_widget(tab.layout,QtWidgets.QLabel('folder:'),
                         spec='small-left')
    self.folderBox = QtWidgets.QComboBox(self)
    self.folderBox.addItems(FOLDERS.keys())
    self.add_side_widget(tab.layout, self.folderBox, spec='large-right')
        
    self.folderButton = QtWidgets.QPushButton("Open folder [Ctrl+O]", self)
    self.folderButton.clicked.connect(self.open_intrinsic_folder)
    self.add_side_widget(tab.layout,self.folderButton, spec='large-left')
    self.lastBox = QtWidgets.QCheckBox("last ")
    self.lastBox.setStyleSheet("color: gray;")
    self.add_side_widget(tab.layout,self.lastBox, spec='small-right')
    self.lastBox.setChecked(True)

    self.add_side_widget(tab.layout,QtWidgets.QLabel('  - protocol:'),
                    spec='large-left')
    self.numBox = QtWidgets.QComboBox(self)
    self.numBox.addItems(['sum']+[str(i) for i in range(1,10)])
    self.add_side_widget(tab.layout,self.numBox,
                    spec='small-right')

    self.add_side_widget(\
            tab.layout,QtWidgets.QLabel('  - spatial-subsampling (pix):'),
            spec='large-left')
    self.ssBox = QtWidgets.QLineEdit()
    self.ssBox.setText('0')
    self.add_side_widget(tab.layout,self.ssBox, spec='small-right')

    self.loadButton = QtWidgets.QPushButton(" === load data === ", self)
    self.loadButton.clicked.connect(self.load_SS_intrinsic_data)
    self.add_side_widget(tab.layout,self.loadButton)

    # -------------------------------------------------------
    self.add_side_widget(tab.layout,QtWidgets.QLabel(''))

    self.pmButton = QtWidgets.QPushButton(\
            " == compute power maps == ", self)
    self.pmButton.clicked.connect(self.compute_SS_power_maps)
    self.add_side_widget(tab.layout,self.pmButton)
   
    self.add_side_widget(tab.layout,QtWidgets.QLabel('scale: '), 'small-left')
    self.scaleButton = QtWidgets.QDoubleSpinBox(self)
    self.scaleButton.setRange(0, 10)
    self.scaleButton.setSuffix(' (mm, image height)')
    self.scaleButton.setValue(2.7)
    self.add_side_widget(tab.layout,self.scaleButton, 'large-right')

    self.add_side_widget(tab.layout,QtWidgets.QLabel('angle: '), 'small-left')
    self.angleButton = QtWidgets.QSpinBox(self)
    self.angleButton.setRange(-360, 360)
    self.angleButton.setSuffix(' (°)')
    self.angleButton.setValue(15)

    self.add_side_widget(tab.layout,self.angleButton, 'small-middle')
    self.pdfButton = QtWidgets.QPushButton("PDF", self)
    self.pdfButton.clicked.connect(self.pdf_intrinsic)
    self.add_side_widget(tab.layout,self.pdfButton, 'small-right')

    # -------------------------------------------------------
    self.add_side_widget(tab.layout,QtWidgets.QLabel('Image 1: '), 'small-left')
    self.img1Button = QtWidgets.QComboBox(self)
    self.add_side_widget(tab.layout,self.img1Button, 'large-right')
    self.img1Button.currentIndexChanged.connect(self.update_img1)

    self.add_side_widget(tab.layout,QtWidgets.QLabel('Image 2: '), 'small-left')
    self.img2Button = QtWidgets.QComboBox(self)
    self.add_side_widget(tab.layout,self.img2Button, 'large-right')
    self.img2Button.currentIndexChanged.connect(self.update_img2)

    # ========================================================
    #------------------- THEN MAIN PANEL   -------------------

    self.graphics_layout= pg.GraphicsLayoutWidget()

    tab.layout.addWidget(self.graphics_layout,
                         0, self.side_wdgt_length,
                         self.nWidgetRow, 
                         self.nWidgetCol-self.side_wdgt_length)

    self.raw_trace = self.graphics_layout.addPlot(row=0, col=0, rowspan=1, colspan=23)
    
    self.spectrum_power = self.graphics_layout.addPlot(row=1, col=0, rowspan=2, colspan=9)
    self.spDot = pg.ScatterPlotItem()
    self.spectrum_power.addItem(self.spDot)
    
    self.spectrum_phase = self.graphics_layout.addPlot(row=1, col=9, rowspan=2, colspan=9)
    self.sphDot = pg.ScatterPlotItem()
    self.spectrum_phase.addItem(self.sphDot)

    # images
    self.img1B = self.graphics_layout.addViewBox(row=3, col=0,
                                                 rowspan=10, colspan=10,
                                                 lockAspect=True, invertY=True)
    self.img1 = pg.ImageItem()
    self.img1B.addItem(self.img1)

    self.img2B = self.graphics_layout.addViewBox(row=3, col=10,
                                                 rowspan=10, colspan=9,
                                                 lockAspect=True, invertY=True)
    self.img2 = pg.ImageItem()
    self.img2B.addItem(self.img2)

    for i in range(3):
        self.graphics_layout.ci.layout.setColumnStretchFactor(i, 1)
    self.graphics_layout.ci.layout.setColumnStretchFactor(3, 2)
    self.graphics_layout.ci.layout.setColumnStretchFactor(12, 2)
    self.graphics_layout.ci.layout.setRowStretchFactor(0, 3)
    self.graphics_layout.ci.layout.setRowStretchFactor(1, 4)
    self.graphics_layout.ci.layout.setRowStretchFactor(3, 5)
        
    # -------------------------------------------------------
    self.pixROI = pg.ROI((0, 0), size=(10,10),
                         pen=pg.mkPen((255,0,0,255)),
                         rotatable=False,resizable=False)
    self.pixROI.sigRegionChangeFinished.connect(self.moved_pixels)
    self.img1B.addItem(self.pixROI)

    self.refresh_tab(tab)

    self.data = None

    self.show()
    
def set_pixROI(self):

    if self.data is not None:

        img = self.data[0,:,:]
        self.pixROI.setSize((img.shape[0]/10., img.shape[1]/10))
        xpix, ypix = get_pixel_value(self)
        self.pixROI.setPos((int(img.shape[0]/2), int(img.shape[1]/2)))

def get_pixel_value(self):

    y, x = int(self.pixROI.pos()[0]), int(self.pixROI.pos()[1])

    return x, y
    
def moved_pixels(self):

    for plot in [self.raw_trace, self.spectrum_power, self.spectrum_phase]:
        plot.clear()

    if self.data is not None:
        show_raw_data(self)         

def update_img(self, img, imgButton):

    if imgButton.currentText() in self.IMAGES:

        img.setImage(self.IMAGES[imgButton.currentText()].T)

        if 'power' in imgButton.currentText():
            img.setLookupTable(power_color_map)
        else:
            img.setLookupTable(signal_color_map)

def update_img1(self):
    update_img(self, self.img1, self.img1Button)

def update_img2(self):
    update_img(self, self.img2, self.img2Button)


def update_imgButtons(self):

    self.img1Button.clear()
    self.img2Button.clear()

    self.img1Button.addItems([f for f in self.IMAGES.keys() if 'func' not in f])
    self.img2Button.addItems([f for f in self.IMAGES.keys() if 'func' not in f])

   
def reset(self):

    self.IMAGES = {}

def load_single_datafile(datafile, params):

    io = pynwb.NWBHDF5IO(datafile, 'r')
    nwbfile = io.read()
    t, x = nwbfile.acquisition['image_timeseries'].timestamps[:].astype(np.float64),\
        nwbfile.acquisition['image_timeseries'].data[:,:,:].astype(np.uint16)
    interp_func = interp1d(t, x, axis=0, kind='nearest', fill_value='extrapolate')
    dt = 5e-2 # 20Hz regular sampling
    new_t = np.arange(int(params['period']*params['Nrepeat']/dt))*dt
    io.close()
    return new_t, interp_func(new_t)


def load_raw_data(datafolder, run_id):

    params = np.load(os.path.join(datafolder, 'metadata.npy'),
                     allow_pickle=True).item()

    if run_id=='sum':
        Data, n = None, 0
        for i in range(1, 15): # no more than 15 repeats...(but some can be removed, hence the "for" loop)
            if os.path.isfile(os.path.join(datafolder, 'SS-intrinsic-%i.nwb' % i)):
                t, data  = load_single_datafile(os.path.join(datafolder, 'SS-intrinsic-%i.nwb' % i), params)
                if Data is None:
                    Data = data
                    n = 1
                else:
                    Data += data
                    n+=1
        if n>0:
            return params, (t, Data/n)
        else:
            return params, (None, None)

    elif os.path.isfile(os.path.join(datafolder, 'SS-intrinsic-%s.nwb' % (run_id))):
        return params, load_single_datafile(os.path.join(datafolder, 'SS-intrinsic-%s.nwb' % (run_id)), params)
    else:
        print('"%s" file not found' % os.path.join(datafolder, 'SS-intrinsic-%s.nwb' % (run_id)))



def load_SS_intrinsic_data(self):
    
    tic = time.time()

    datafolder = get_datafolder(self)

    print(datafolder)
    if os.path.isdir(datafolder):

        print('- loading and preprocessing data [...]')

        # clear previous plots
        for plot in [self.raw_trace, self.spectrum_power, self.spectrum_phase]:
            plot.clear()

        # load data
        self.params, (self.t, self.data) = load_raw_data(datafolder, self.numBox.currentText())

        if float(self.ssBox.text())>0:

            print('    - spatial subsampling [...]')
            self.data = intrinsic_analysis.resample_img(self.data,
                                                        int(self.ssBox.text()))
            

        vasc_img = os.path.join(get_datafolder(self), 'vasculature.npy')
        if os.path.isfile(vasc_img):
            if float(self.ssBox.text())>0:
                self.IMAGES['vasculature'] = intrinsic_analysis.resample_img(\
                                                    np.load(vasc_img),
                                                    int(self.ssBox.text()))
            else:
                self.IMAGES['vasculature'] = np.load(vasc_img)

        self.IMAGES['raw-img-start'] = self.data[0,:,:]
        self.IMAGES['raw-img-mid'] = self.data[int(self.data.shape[0]/2.)-1,:,:]
        self.IMAGES['raw-img-stop'] = self.data[-2,:,:]
       
        update_imgButtons(self)

        set_pixROI(self) 
        show_raw_data(self)

        print('- data loaded !    (in %.1fs)' % (time.time()-tic))

    else:
        print(' Data "%s" not found' % datafolder)


def show_raw_data(self):
    
    # clear previous plots
    for plot in [self.raw_trace, self.spectrum_power, self.spectrum_phase]:
        plot.clear()

    xpix, ypix = get_pixel_value(self)

    new_data = self.data[:,xpix, ypix]

    self.raw_trace.plot(self.t, new_data)

    spectrum = np.fft.fft((new_data-new_data.mean())/new_data.mean())
    power, phase = np.abs(spectrum), (2*np.pi+np.angle(spectrum))%(2.*np.pi)-np.pi

    power, phase = np.abs(spectrum), np.angle(spectrum)

    x = np.arange(len(power))
    self.spectrum_power.plot(np.log10(x[1:]), np.log10(power[1:]))
    self.spectrum_phase.plot(np.log10(x[1:]), phase[1:])
    self.spectrum_power.plot([np.log10(x[int(self.params['Nrepeat'])])],
                             [np.log10(power[int(self.params['Nrepeat'])])],
                             size=10, symbolPen='g',
                             symbol='o')
    self.spectrum_phase.plot([np.log10(x[int(self.params['Nrepeat'])])],
                             [phase[int(self.params['Nrepeat'])]],
                             size=10, symbolPen='g',
                             symbol='o')

def compute_SS_power_maps(self):

    print('- computing power maps [...]')

    maps = {}
    maps['power'], _ = intrinsic_analysis.perform_fft_analysis(self.data,
                                                    self.params['Nrepeat'])


    fig, ax = plt.subplots(figsize=(4,2.3))
    intrinsic_analysis.plot_power_map(ax, fig, maps['power'])
    print(' -> power maps calculus done !')

    plt.show()
    update_imgButtons(self)
    

def save_SS_intrinsic(self):

    if self.data is not None:

        np.save(os.path.join(self.datafolder, '..', '..', '%s_ISImaps.npy' % self.subject),
                self.data)
        print('\n         current maps saved as: ', \
           os.path.join(self.datafolder, '..', '..', '%s_ISImaps.npy' % self.subject))

    else:
        print(' need to perform Area Segmentation first ')


def get_datafolder(self):

    if self.lastBox.isChecked():
        try:
            self.datafolder = last_datafolder_in_dayfolder(day_folder(FOLDERS[self.folderBox.currentText()]),
                                                           with_NIdaq=False)
        except FileNotFoundError:
            pass # we do not update it
        #
    if self.datafolder=='':
        print('need to set a proper datafolder !')

    return self.datafolder
    

def pdf_intrinsic(self):

    cmd = '%s -m physion.intrinsic.pdf %s' % (python_path, self.datafolder)
    cmd += ' --output %s' % os.path.join(FOLDERS[self.folderBox.currentText()], self.subject+'.pdf')
    cmd += ' --image_height %.1f ' % self.scaleButton.value()
    cmd += ' --angle_from_rig %.1f ' % self.angleButton.value()

    cwd = os.path.join(pathlib.Path(__file__).resolve().parents[3], 'src')
    print('\n launching the command \n :  %s \n ' % cmd)
    p = subprocess.Popen(cmd,
                         cwd=cwd,
                         shell=True)

