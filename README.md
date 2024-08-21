# Coffee Machine Simulator

This repository contains a Python project for a coffee machine simulator. The simulator allows users to select and make different types of coffee, while managing resources and handling payments.

## Project Overview

The coffee machine simulator includes the following features:

- **Menu**: Provides options for different types of coffee including espresso, latte, and cappuccino.
- **Coffee Maker**: Handles the preparation of coffee, checking if sufficient resources are available.
- **Money Machine**: Manages payment processing and financial reporting.

## How It Works

1. **Menu**: Displays the available coffee options and their prices.
2. **Order**: The user can place an order by typing the name of the coffee they want.
3. **Reporting**: Users can check the current status of resources and financials by typing `report`.
4. **Turn Off**: The coffee machine can be turned off by typing `off`.

## Installation

To set up and run the coffee machine simulator, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/coffee-machine-simulator.git
   cd coffee-machine-simulator
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```
  
3. **Activate the Virtual Environment**:
  ```bash
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
  ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Simulator**:
   ```bash
   python main.py
   ```

## Usage

After running the simulator with `python main.py`, follow the on-screen prompts to interact with the coffee machine:

1. **View Menu**: The available coffee options and their prices will be displayed.
2. **Place Order**: Type the name of the coffee you want to order (e.g., `espresso`, `latte`, or `cappuccino`).
3. **Check Report**: Type `report` to view the current status of resources and financials.
4. **Turn Off**: Type `off` to turn off the coffee machine.

## Dependencies

The project relies on the following Python packages:

- `menu` (for handling the coffee menu)
- `coffee_maker` (for managing coffee preparation)
- `money_machine` (for handling payments and financial reporting)

Dependencies are listed in `requirements.txt` for easy installation.

## Contributing

Feel free to fork this repository and submit pull requests if you would like to add new features or improve the code. Contributions are welcome!
