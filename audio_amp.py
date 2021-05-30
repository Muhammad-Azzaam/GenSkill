import struct


def amplify(fin,fout,change):
	fname = open(fin, "rb")
	amp_name = open(fout, "wb")
	
	header = fname.read(44)
	amp_name.write(header)
	
	block = fname.read(2)
	
	while block:
		unp_block = struct.unpack('h', block)
		val = unp_block[0]		
		val*=change
		val = int(val)
		pack_block = struct.pack('h', val)
		amp_name.write(pack_block)
		block = fname.read(2)
		
	fname.close()
	amp_name.close()




def main():
	fin = input("Enter the name of the file to be amplified: ")
	fout = input("Enter the name of the new amplified file: ")
	change = input("Enter the amplification rate: ")
	change = float(change)
	
	amplify(fin,fout,change)
	


main()
