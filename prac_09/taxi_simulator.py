# taxi_simulator.py
"""
CP1404/CP5632 Practical - Taxi Simulator
This program simulates a taxi service where the user can choose a taxi,
drive it, and see the cost of each trip.

The program includes:
- A Taxi class
- A SilverServiceTaxi class
- Polymorphism to handle different types of taxis
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

# Constants for taxi fare and flagfall amounts
REGULAR_FARE = 1.23
FLAGFALL = 4.50
SILVER_SERVICE_FARE = 2.46
LUXURY_FARE = 4.92

