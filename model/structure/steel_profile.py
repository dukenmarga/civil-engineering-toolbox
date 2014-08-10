
class Steel_Profile:
    def iwf_table(self):
        data = {
            'geometricProperties': {}
        }
        self.iwf_profiles = [
            "H-100x100x6x8",
            "H-200x200x8x12"
        ]

        for profile in self.iwf_profiles:
            split1 = profile[2:]
            dim = split1.split('x')
            tw = int(dim[2])
            tf = int(dim[3])
            h = int(dim[0])-2*tf
            b = int(dim[1])
            data['geometricProperties'][profile] = {
                'profileName': profile,
                'Ixx': ( h**3*tw/12. + 2*(tf*b/12. + tf*b*(h+tf)**2/4.) )/10000,
                'tes' : 's'
            }
        return data