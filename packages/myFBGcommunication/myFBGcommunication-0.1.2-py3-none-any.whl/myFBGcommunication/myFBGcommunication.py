# 0.1.2
import time
import numpy as np
import serial
import scipy
import pandas as pd
import importlib.resources
import os
import matplotlib.pyplot as plt
import numpy as np

# 備忘：lineの内訳
# オンボード計算がFalseのとき→ [ピークの位置(4Byte), アンプ量(4Byte)]*チャンネル数 + [温度(℃*100)(2Byte), 空(2Byte), 不明(計4Byte)] + ["Ende"(4Byte)]
# →出力は8×チャンネル数+12byte

class FBGcom:
    def __init__(self):
        self._ser: serial.serialwin32.Serial = None
        self.FBG_num = 0
        self.WL_ranges = []
        self._iniPath = importlib.resources.path('myFBGcommunication', 'params.ini')
        self._iniPath = str(self._iniPath.args[0])
        if os.path.isfile(self._iniPath):
            self._params = pd.read_csv(self._iniPath, header=None, index_col=0)
        else:
            self._iniPath = 'params.ini'
            if not os.path.isfile(self._iniPath):
                self._make_default_paramsfile()
            self._params = pd.read_csv(self._iniPath, header=None, index_col=0)
        self._FBG_width = float(self._params.loc['FBG_width', 1])   # nano m
        self._integration_time = float(self._params.loc['integration_time', 1])
        self._Averaging = int(self._params.loc['Averaging', 1])
        self._on_boradCalculation = bool(self._params.loc['on_boradCalc', 1])
        self._defaultTemp = float(self._params.loc['defaultTemp', 1])
        self._sample_time = float(self._params.loc['sample_time',1])
        self._spectrum = []
        self._WLL = []

    def init(self, COM):
        try:
            self._ser = serial.Serial(COM, baudrate=3000000,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                timeout=0.001)
            self._ser.write(b'?>')
            time.sleep(0.1)
            device_name = self._ser.read_all()
            if len(device_name) == 0:
                return -1
        except serial.serialutil.SerialException:
            return -1

        self.auto_setting()
        self.set_param()
        return 1


    def auto_setting(self):
        # ----FBGセンサの検出-----
        while len(self._ser.read_all()) != 0:
            pass
        spectrum_raw = b''
        WLL_raw = b''
        self._ser.write(b's>')
        self._ser.flush()
        while len(spectrum_raw) != 2052:
            spectrum_raw += self._ser.read_all()
        self._spectrum = [int.from_bytes(spectrum_raw[i*2:i*2+2], byteorder='little') for i in range(1024)]
        self._spectrum[0:3] = [self._spectrum[3]]*3
        _peaks, _ = scipy.signal.find_peaks(self._spectrum, height=5000, distance=50)
        _peaks = _peaks[1:]
        self.FBG_num = len(_peaks)
        if self.FBG_num == 0:
            return -1
        while len(self._ser.read_all()) != 0:
            pass
        self._ser.write(b'WLL>')  # Get wavelength of pixels list
        self._ser.flush()
        while len(WLL_raw) != 4100:
            WLL_raw += self._ser.read_all()
        # --バイナリで出てくる全波長の変換--
        self._WLL = [int.from_bytes(WLL_raw[i*4:i*4+4], byteorder='little') for i in range(1024)]
        # --ピーク値の波長--
        self._FBG_wavelength = [self._WLL[i] for i in _peaks]

        # ----アクティブチャンネルの設定-----
        for i, nowFBG_wavelength in enumerate(self._FBG_wavelength):
            # 各チャンネルの検出範囲を設定
            now_WL_range = [int(nowFBG_wavelength - (self._FBG_width * 10000) / 2), int(nowFBG_wavelength + (self._FBG_width * 10000) / 2)]
            self.WL_ranges.append(now_WL_range)
            send = 'Ke,' + str(i) + ',' + str(now_WL_range[0]) + ',' + str(now_WL_range[1]) + '>'
            self._ser.write(send.encode())
            self._ser.flush()
        # チャンネル数の設定
        send = 'KA,' + str(self.FBG_num) + '>'
        self._ser.flush()
        self._ser.write(send.encode())
        return 1

    def set_param(self, FBG_width=None, integration_time=None, Averaging=None, on_boradCalculation=None, defaultTemp=None, sample_time=None,WL_range=False):
        self._params = pd.read_csv(self._iniPath, header=None, index_col=0)
        if FBG_width == None:
            self._FBG_width = float(self._params.loc['FBG_width', 1])   # nano m
        else:
            self._FBG_width = FBG_width
        if integration_time == None:
            self._integration_time = float(self._params.loc['integration_time', 1])
        else:
            self._integration_time = integration_time
        if Averaging == None:
            self._Averaging = int(self._params.loc['Averaging', 1])
        else:
            self._Averaging = Averaging
        if on_boradCalculation == None:
            self._on_boradCalculation = bool(self._params.loc['on_boradCalc', 1])
        else:
            self._on_boradCalculation = on_boradCalculation
        if defaultTemp == None:
            self._defaultTemp = float(self._params.loc['defaultTemp', 1])
        else:
            self._defaultTemp = defaultTemp
        if sample_time == None:
            self._sample_time = float(self._params.loc['sample_time', 1])
        else:
            self._sample_time = sample_time
        # if WL_range:
        #     self.WL_ranges
        self._params.to_csv(self._iniPath, header=None)

        # 露光時間，平均化処理のパラメータ設定
        send = 'iz,' + str(int(self._integration_time * 1000000)) + '>'
        time.sleep(0.01)
        self._ser.write(send.encode())

        send = 'm,' + str(self._Averaging) + '>'
        self._ser.write(send.encode())
        time.sleep(0.01)
        self._ser.write(b'LED,1>')
        time.sleep(0.01)
        self._ser.write(b'a>')
        for i in range(self.FBG_num):
            send = 'OBsType,' + str(i) + ',' + '0' + '>'
            self._ser.write(send.encode())
        self._ser.write(b'OBN>')  # zero Temp/strain
        time.sleep(0.01)
        send = 'OBsaT0,' + str(int(self._defaultTemp*100)) + '>'
        self._ser.write(send.encode())  # 全チャネルに同じT0値を設定
        time.sleep(0.01)
        send = 'OBB,' + str(int(self._on_boradCalculation)) + '>'
        self._ser.write(send.encode())
        time.sleep(0.01)

        self._ser.write(b'P>')
        while self._ser.readline() != b'':
            pass

    def read(self, Targets):
        tmp_line = b''
        data_len = 8 * self.FBG_num + 12  # (ひずみデータ4bit ＋ 温度データ4bit)*FBGの数
        dataOK = False
        while not dataOK:
            line = tmp_line
            tmp_line = b''
            self._ser.write(b'P>')
            self._ser.flush()
            while len(line) < data_len:
                time.sleep(self._sample_time)
                line += self._ser.read_all()
                self._ser.write(b'P>')
            if len(line) == data_len:
                if line[-4:-1] == b'End':
                    dataOK = True
                else:
                    print('CHECK1')
            elif len(line) > data_len:
                ende_idx = line.find(b'Ende')
                tmp_line = line[ende_idx + 4:len(line)]
                if ende_idx != data_len - 4:
                    line = line[-data_len:]
                else:
                    tmp_line = line[ende_idx + 4:len(line)]
                    line = line[0:ende_idx + 4]
                    dataOK = True
        if self._on_boradCalculation:
            now_data = [int.from_bytes(line[8 * (i+1):8 * (i+1) + 4], byteorder='little', signed=True)/10000 for i in Targets]
        else:
            now_data = [int.from_bytes(line[8 * (i+1):8 * (i+1) + 4], byteorder='little', signed=True) for i in Targets]
        return now_data

    def read_all(self):
        now_data = self.read(range(self.FBG_num-1))
        return now_data

    def show_spectrum(self):
        for i in range(self.FBG_num):
            wll = np.arange(self.WL_ranges[i][0],self.WL_ranges[i][1])
            plt.fill_between(wll, np.max(self._spectrum)*2, fc="lightgray")
        plt.plot(self._WLL, self._spectrum)
        plt.ylim([0, np.max(self._spectrum)*1.1])
        plt.show()

    def _make_default_paramsfile(self):
        _paramas = [['FBG_width',3.0],
                    ['integration_time',0.05],
                    ['Averaging',1],
                    ['on_boradCalc',True],
                    ['defaultTemp',21],
                    ['sample_time',0.001]]
        pd.DataFrame(_paramas, columns=None).to_csv('params.ini', index=None, header=None)
