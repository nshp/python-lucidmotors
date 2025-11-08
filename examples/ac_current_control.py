#!/usr/bin/env python3
"""
Example script demonstrating AC current control functionality.

This script shows how to:
1. Set the AC current limit for a vehicle
2. Get the current AC current settings
3. Monitor changes in AC current settings

Requirements:
- Python 3.7+
- lucidmotors package installed
- Valid Lucid account credentials
"""

import asyncio
import logging
from lucidmotors import LucidAPI

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    """Main function demonstrating AC current control."""

    # Initialize the API client
    async with LucidAPI(auto_wake=True) as api:
        try:
            # Login with your credentials
            logger.info("Logging in...")
            await api.login("your_email@example.com", "your_password")
            logger.info("Login successful!")

            # Get your vehicles
            vehicles = await api.fetch_vehicles()
            if not vehicles:
                logger.error("No vehicles found in your account")
                return

            vehicle = vehicles[0]  # Use the first vehicle
            logger.info(f"Using vehicle: {vehicle.vehicle_id}")

            # Get current AC current settings
            logger.info("Getting current AC current settings...")
            current_settings = await api.get_ac_current_settings(vehicle)

            logger.info("Current AC Current Settings:")
            logger.info(
                f"  Active Session Limit: {current_settings['active_session_limit']}A"
            )
            logger.info(f"  Energy Limit: {current_settings['energy_limit']}A")
            logger.info(f"  Requested Limit: {current_settings['requested_limit']}A")

            # Example: Set AC current limit to 32A (common for home charging)
            new_limit = 32
            logger.info(f"Setting AC current limit to {new_limit}A...")
            await api.set_ac_current_limit(vehicle, new_limit)
            logger.info("AC current limit set successfully!")

            # Wait a moment for the change to take effect
            await asyncio.sleep(2)

            # Get updated settings to confirm the change
            logger.info("Getting updated AC current settings...")
            updated_settings = await api.get_ac_current_settings(vehicle)

            logger.info("Updated AC Current Settings:")
            logger.info(
                f"  Active Session Limit: {updated_settings['active_session_limit']}A"
            )
            logger.info(f"  Energy Limit: {updated_settings['energy_limit']}A")
            logger.info(f"  Requested Limit: {updated_settings['requested_limit']}A")

            # Example: Set AC current limit to 16A (lower power charging)
            lower_limit = 16
            logger.info(f"Setting AC current limit to {lower_limit}A...")
            await api.set_ac_current_limit(vehicle, lower_limit)
            logger.info("AC current limit set successfully!")

            # Wait and get final settings
            await asyncio.sleep(2)
            final_settings = await api.get_ac_current_settings(vehicle)

            logger.info("Final AC Current Settings:")
            logger.info(
                f"  Active Session Limit: {final_settings['active_session_limit']}A"
            )
            logger.info(f"  Energy Limit: {final_settings['energy_limit']}A")
            logger.info(f"  Requested Limit: {final_settings['requested_limit']}A")

        except Exception as e:
            logger.error(f"Error: {e}")
            raise


if __name__ == "__main__":
    print("AC Current Control Example")
    print("=" * 30)
    print(
        "This script demonstrates how to control AC current limits for your Lucid vehicle."
    )
    print("Make sure to update the credentials in the script before running.")
    print()

    # Run the example
    asyncio.run(main())
