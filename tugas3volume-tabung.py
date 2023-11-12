if __name__ == "_main_":
         input_str = input ("masukkan diameter tabun: ")
         diameter = float(input_str)
         input_str = input("masukan tinggi tabung: ")
         t = float(input_str)
         pi = 22.0/7.0
         r = diameter/2
         print("volume tabung dengan diameter {} dan tinggi {} adalah: {}" .format(diameter, t, pi*r**2*t))
