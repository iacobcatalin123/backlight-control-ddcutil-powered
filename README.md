# Backlight Control ddcutil powered

For linux users to who's displays simply dont work to other options than ddcutil to control the BACKLIGHT not the software light idk something

## The UI
![ui](https://i.imgur.com/J9Z1Zjc.png)

## -cmd for cli

will increase all monitors brightness by 10
```bash
sudo python3 main.py -cmd + 10 
```


### Errors:
- In case of i2c-dev missing you can load it using: `sudo modprobe i2c-dev` . to check if it's loaded use: `lsmod | grep i2c_dev`
