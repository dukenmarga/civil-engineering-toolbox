class Earthquake:
    def __init__(self):
        self.data = {
            'properties': []
        }
    def response_spectrum(self, ss, s1, soil_class):
        """ Generate response spectrum based on ASCE 7-2010
        """

        self.data = {
            'ss': ''
        }
        if soil_class == "SA":
            fa = 0.8
            fv = 0.8
        elif soil_class == "SB":
            fa = 1.0
            fv = 1.0
        elif soil_class == "SC":
            # fa
            if ss <= 0.5:
                fa = 1.2
            elif ss > 0.5 and ss < 1.0:
                fa = -0.4*ss+1.4
            else:
                fa = 1.0
            # fv
            fv = -s1+1.8
        elif soil_class == "SD":
            #fa
            if ss <= 0.25:
                fa = 1.6
            elif ss > 0.25 and ss < 0.75:
                fa = -0.88*ss+1.8
            elif ss >= 0.75 and ss < 1.25:
                fa = -0.4*ss+1.5
            else:
                fa = 1.0
            # fv
            if s1 <= 0.1:
                fv = 2.4
            elif s1 > 0.1 and s1 < 0.3:
                fv = -4*s1+2.8
            elif s1 >= 0.3 and s1 < 0.4:
                fv = -2*s1+2.4
            elif s1 >= 0.4 and s1 < 0.5:
                fv = -s1+2
            else:
                fv = 1.5
        else:
            # fa
            if ss <= 0.25:
                fa = 2.5
            elif ss > 0.25 and ss < 0.5:
                fa = -0.32*ss+3.3
            elif ss >= 0.5 and ss < 0.75:
                fa = -2*ss+2.7
            elif ss >= 0.75 and ss < 1.0:
                fa = -1.32*ss+2.1
            else:
                fa = 0.9
            # fv
            if s1 <= 0.1:
                fv = 3.5
            elif s1 > 0.1 and s1 < 0.2:
                fv = -3*s1+3.8
            elif s1 >= 0.2 and s1 < 0.4:
                fv = -4*s1+4
            else:
                fv = 2.4

        # sms and sm1
        sms = ss*fa
        sm1 = s1*fv

        # sds sd1 $s0
        sds = sms*2/3
        sd1 = sm1*2/3
        s0 = sds/2.5

        # T0, Ts
        t0 = 0.2*sd1/sds
        t_ = ts = sd1/sds

        # calculate another point
        x = [0, t0, ts]
        y = [s0, sds, sds]
        while t_ <= 8:
            x.append(t_)
            y.append(sd1/t_)
            t_ += 0.1

        # data[]
        # data['ss'] = ss
        # data['s1'] = s1
        # data['kelas_situs'] = soil_class
        # data['fa'] = fa
        # data['fv'] = fv
        # data['sms'] = sms
        # data['sm1'] = sm1
        # data['sds'] = sds
        # data['sd1'] = sd1
        # data['s0'] = s0
        # data['t0'] = t0
        # data['ts'] = ts
        # data['t'] = t
        # if t>0 and t<t0:
        #     pass
        # elif t>t0 and t<ts:
        #     sa = sds
        # else:
        #     sa = sd1/t
        # data['sa'] = sa

        return x, y
