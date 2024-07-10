Raspberry Pi Project with MCP23S08 and MCP3208

This project involves a Raspberry Pi controlling multiple MCP23S08 and MCP3208 chips along with LEDs. The project includes a Python-based interface for communication and control using classes for MCP23S08 and MCP3208, a test script, and a configuration fiel in TOML format.

Preliminary Configuration

Before starting, you need to enable the SPI function on your Raspberry Pi using 'raspi-config'.
The Raspberry Pi have 2 different SPI bus: one will be known as /dev/spi0.* and the other as /dev/spi1.*.

Enabling SPI1

if '/dev/spi1.0' and '/dev/spi1.1' are not available, you need to enable SPI1 manually:

1. Edit the boot configuration file:

sudo nano /boot/config.txt

2. Add the following lines at the end of the file to enable SPI1:

dtparam=spi=on
dtoverlay=spi1-3cs

3. Save the file and exit the editor (Ctrl + O, Enter, Ctrl + X)
4. Reboot your Raspberry Pi to apply the changes:

sudo reboot

After rebooting, you should see '/dev/spi1.0' and '/dev/spi1.1' available for use.

Install dependencies:

sudo apt-get update 
sudo apt-get install python3-pip
pip3 install spidev RPi-GPIO toml 

Using the MCP23S08 with Raspberry Pi

Introduction

The MCP23S08 is an 8-bit I/O expander that uses the SPI interface to communicate with a microcontroller such as a Raspberry Pi. It allows you to add extra input/output ports to your project, controllable via the SPI bus.

Communication with MCP23S08

To communicate with MCP23S08, you need to send and receive data via the SPI interface. Here is how you can read from and write to the the MCP23S08 registers using Pyhton with the 'spidev' library.

Understanding MCP23S08 Communication

Commmand Structure

Communication with the MCP23S08 involves sending a sequence of bytes over the SPI interface. 
Each command generally consists of the following parts:

- Opcode: Determines whether the operation is a read or write
- Register Address: Specifies which register to access
- Data: The value to write to the register (for write operations)

Opcode

Write Opcode: Ox40 (A0=0, A1=0)
Read Opcode: 0x41 (A0=0, A1=0)

The opcode is followed by the register address and then the data byte

Register Address

The MCP23S08 has several registers for configuring and controlling the I/Os. Here are some key registers:

- IODIR (0X00): I/O Direction Register (1 = input, 0 = output)
- GPIO (0x09): GPIO Register (read/write I/O values)
- OLAT (0x0A): Output Latch Register (maintain output values)

Data 

The data byte is the value you write to the register. For read operations, the data byte received from the MCP23S08 will contain the registers's current value. 

Connecting to the Raspberry Pi via SSH

To interact with the Raspberry Pi remotely, you can use SSH. Here's how to set up and use SSH to connect from your computer.

Connect from Windows:

Open Command Prompt or PowerShell:

ssh pi@192.168.137.220

Connect from Mac or Linux:

Open terminal:

ssh pi@192.168.137.220

When prompted, enter the password for the 'pi' user which is 'raspberry'.





