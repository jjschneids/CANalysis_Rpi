# CANalysis_Rpi
Raspberry Pi 2b CAN data analyzer

Part Requirements:
1. Raspberry Pi 2b (or with equivalent GPIO)
2. MCP2515 CAN transceiver module
3. Jumper wires

#Important Setup bash commands:
sudo apt update
sudo apt upgrade
sudo apt install can-utils

#A good Tutorial, but it gets some stuff wrong for our case:
https://vimtut0r.com/2017/01/17/can-bus-with-raspberry-pi-howtoquickstart-mcp2515-kernel-4-4-x/

Use the lines in the _config.txt_ instead of the lines in the tutorial if they don't work.
Also, the VCC on your CAN Transciever should be connected to the 5V of your RPi rather than another external 5V source.
Also, double check wire connections if you get errors.

#Useful can-utils bash commands:

To show anything that is received by the transceiver run the following in bash:

```bash
candump can0
```

or you can add timestamps to the messages with the following:
```bash
candump -t a can0
```

Then you can pipe the output to a file via:
```bash
candump -t a can0 > FILENAME.txt
```

Look at the can-utils [documentation](https://github.com/linux-can/can-utils) for more information.
