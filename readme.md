# IMechE-Design-Challenge-2025

This repository is a fork of [IMechE-Design-Challenge-2024](https://github.com/shehan-m/IMechE-Design-Challenge-2024)

Documentation is in branch docs

## Installation

OS: Raspberry Pi OS (Legacy, 32-bit) Lite

- **Step 1:** \
  To download code, it is necessary to have git installed:

```bash
sudo apt update && sudo apt-get install git -y
```

- **Step 2:** \
  Now install prerequisites for firmware:

```bash
sudo apt install python3-opencv fswebcam
```

- **Step 3:** \
  Once these are installed, use the following command to clone the repo into the home directory:

```bash
cd && git clone https://github.com/js0ny/IMechE-Design-Challenge-2025/
```

## How to run code on startup

- **Step 1:** \
  Open the `rc.local` file using nano editor:

```bash
cd ~ && sudo nano /etc/rc.local
```

- **Step 2:** \
  Make bash script executable:

```bash
sudo chmod +x /IMechE-Design-Challenge-2025/Firmware/startup.sh
sudo echo "sudo chmod +x /IMechE-Design-Challenge-2025/Firmware/startup.sh" > /etc/rc.local
```

- **Step 3:** \
  Add the following commands above `exit 0`

```bash
sudo apt-get update && sudo apt-get install git -y
```

## Electronics

### Wiring Diagram

![image](Assets/circuit%20diagram%20v5_bb.png)

### Limit switch

switch type: SPDT

#### This switch has three terminals

- Common (COM): The common terminal
- Normally Open (NO): Connected to COM when the switch is pressed
- Normally Closed (NC): Connected to COM when the switch is not pressed

### Stepper driver current limiting

$V_{\text{ref}} = I_{\text{max}} * 8 * R_{s}$

where, $I_{\text{max}}$ is the current limit of the stepper motor, $Rs$ is the resistance of the current sensing resistor (R5 on driver board)

In our case, $I_{\text{max}}$ is $350 mA$ and $Rs$ is $0.1 \Omega$. Let's run the stepper motor at $60\%$ of its rating. From this we get $V_{\text{ref}}$:

$V_{\text{ref}} = (0.350 * 0.6) * 8 * 0.1 = 0.17 V$
