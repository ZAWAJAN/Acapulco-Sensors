# Compiling Radiance on Raspberry Pi

1. **Basic Install:**
```bash
sudo apt-get install libx11-dev
wget --no-check-certificate http://www.radiance-online.org/software/snapshots/radiance-HEAD.tgz
wget --no-check-certificate http://www.radiance-online.org/download-install/radiance-source-code/latest-release/rad5R0supp.tar.gz
tar -xf radiance-HEAD.tgz
tar -xf rad5R0supp.tar.gz
```
2. **Replace the config.guess file:**
	- Go to the folder where the `config.guess` file is located, it should be `ray/src/px/tiff`
	- Download a new [config.guess](http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD) file and replace the existing one:
	 ```bash
	 cd ray/src/px/tiff
	 wget 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD' -O config.guess
	 ```
3. **Proceed with the install...**
	- Go back to the `ray` folder and install:
	```bash
	cd ../../ray
	sudo ./makeall install
	```
2. **Follow instructions, do not change anything if prompted**
3. **Copy executables:**
	- Verify if executables from Radiance (like `pcomb`) are now in the `/usr/local/bin/` folder, and if not:
	- Copy all executables (like `pcomb`) from `ray/src/px` to `/usr/local/bin/`