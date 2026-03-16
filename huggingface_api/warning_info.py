# =============================================================
# Fix My Ride - Warning Light Information Database
# All 37 classes from car-dashboard-sndt9 dataset
# =============================================================

WARNING_LIGHT_INFO = {

    # ── AIRBAG / SEATBELT ──────────────────────────────────────
    "Airbag and seat belt system": {
        "severity": "Critical",
        "color": "Red",
        "meaning": "There is a fault in the airbag or seatbelt pretensioner system.",
        "action": "Visit a mechanic immediately. Airbags may not deploy in a crash.",
        "category": "Safety"
    },
    "SRS-Airbag": {
        "severity": "Critical",
        "color": "Red",
        "meaning": "Supplemental Restraint System (airbag) fault detected.",
        "action": "Do not ignore. Visit mechanic immediately. Risk of airbag failure in accident.",
        "category": "Safety"
    },
    "Seat Belt": {
        "severity": "High",
        "color": "Red",
        "meaning": "Seatbelt is not fastened.",
        "action": "Fasten your seatbelt before driving.",
        "category": "Safety"
    },
    "Seat belt buckles": {
        "severity": "High",
        "color": "Red",
        "meaning": "One or more seatbelts are unbuckled.",
        "action": "Ensure all passengers have fastened their seatbelts.",
        "category": "Safety"
    },

    # ── BRAKES ────────────────────────────────────────────────
    "Anti Lock Braking System": {
        "severity": "High",
        "color": "Yellow",
        "meaning": "ABS system has detected a fault. Normal braking still works but ABS may not activate.",
        "action": "Drive carefully. Avoid sudden braking. Visit mechanic soon.",
        "category": "Brakes"
    },
    "Anti-lock brake system ABS": {
        "severity": "High",
        "color": "Yellow",
        "meaning": "Anti-lock braking system fault detected.",
        "action": "Normal brakes still work. Avoid harsh braking. Get checked by mechanic.",
        "category": "Brakes"
    },
    "Brake System Issue": {
        "severity": "Critical",
        "color": "Red",
        "meaning": "Serious brake system fault detected. Could be low brake fluid or brake failure.",
        "action": "Stop driving immediately if brakes feel weak. Call mechanic or towing service.",
        "category": "Brakes"
    },
    "Brake system": {
        "severity": "Critical",
        "color": "Red",
        "meaning": "Brake system warning. Could indicate low brake fluid or worn brake pads.",
        "action": "Check brake fluid level. Visit mechanic before driving further.",
        "category": "Brakes"
    },
    "Braking System Issue": {
        "severity": "Critical",
        "color": "Red",
        "meaning": "Fault detected in braking system.",
        "action": "Do not drive at high speed. Visit mechanic immediately.",
        "category": "Brakes"
    },

    # ── ENGINE ────────────────────────────────────────────────
    "Check Engine": {
        "severity": "High",
        "color": "Orange",
        "meaning": "Engine management system has detected a fault. Could be minor or serious.",
        "action": "Get engine scanned for fault codes. Visit mechanic soon.",
        "category": "Engine"
    },
    "Emission control-Engine management lamp": {
        "severity": "Medium",
        "color": "Orange",
        "meaning": "Engine emission or management system issue detected.",
        "action": "Vehicle may be producing excess emissions. Visit mechanic for diagnosis.",
        "category": "Engine"
    },
    "Engine Overheating Warning": {
        "severity": "Critical",
        "color": "Red",
        "meaning": "Engine temperature is critically high. Risk of severe engine damage.",
        "action": "Pull over and stop immediately. Turn off engine. Do not open radiator cap. Call mechanic.",
        "category": "Engine"
    },
    "Engine cooling system": {
        "severity": "Critical",
        "color": "Red",
        "meaning": "Engine cooling system fault. Coolant level may be low or cooling fan failed.",
        "action": "Stop driving. Check coolant level when engine is cool. Visit mechanic.",
        "category": "Engine"
    },
    "High Engine Coolant Temperature": {
        "severity": "Critical",
        "color": "Red",
        "meaning": "Engine coolant temperature is dangerously high.",
        "action": "Pull over immediately. Turn off engine. Let it cool down. Do not continue driving.",
        "category": "Engine"
    },
    "Engine oil pressure": {
        "severity": "Critical",
        "color": "Red",
        "meaning": "Engine oil pressure is critically low. Engine damage can occur within minutes.",
        "action": "Stop the car immediately. Turn off engine. Check oil level. Do not restart without fixing.",
        "category": "Engine"
    },
    "Low Engine Oil Warning": {
        "severity": "High",
        "color": "Orange",
        "meaning": "Engine oil level is low.",
        "action": "Add engine oil as soon as possible. Avoid long drives until oil is topped up.",
        "category": "Engine"
    },

    # ── FUEL ──────────────────────────────────────────────────
    "Low Fuel": {
        "severity": "Medium",
        "color": "Yellow",
        "meaning": "Fuel level is low.",
        "action": "Refuel as soon as possible to avoid running out of fuel.",
        "category": "Fuel"
    },
    "Low fuel level": {
        "severity": "Medium",
        "color": "Yellow",
        "meaning": "Fuel tank is nearly empty.",
        "action": "Visit a fuel station soon. Driving on empty can damage the fuel pump.",
        "category": "Fuel"
    },

    # ── TYRES ─────────────────────────────────────────────────
    "Low Tire Pressure Warning": {
        "severity": "Medium",
        "color": "Yellow",
        "meaning": "One or more tyres have low air pressure.",
        "action": "Check tyre pressures and inflate to recommended level. Inspect for punctures.",
        "category": "Tyres"
    },
    "Tyre pressure monitoring": {
        "severity": "Medium",
        "color": "Yellow",
        "meaning": "Tyre pressure monitoring system has detected low pressure in one or more tyres.",
        "action": "Check all tyre pressures. Inflate or repair as needed.",
        "category": "Tyres"
    },

    # ── CHARGING / BATTERY ────────────────────────────────────
    "Charging System Issue": {
        "severity": "High",
        "color": "Red",
        "meaning": "Vehicle battery is not charging properly. Alternator or battery fault.",
        "action": "Limit electrical usage. Visit mechanic soon to avoid battery drain.",
        "category": "Electrical"
    },
    "Vehicle charging system": {
        "severity": "High",
        "color": "Red",
        "meaning": "Charging system fault. Battery may not be receiving charge.",
        "action": "Check battery and alternator. Visit mechanic before battery dies completely.",
        "category": "Electrical"
    },

    # ── STEERING ──────────────────────────────────────────────
    "Electronic Power Steering": {
        "severity": "High",
        "color": "Yellow",
        "meaning": "Electronic power steering system fault detected.",
        "action": "Steering may feel heavy. Drive carefully and visit mechanic soon.",
        "category": "Steering"
    },
    "Electronic Power Steering Warning": {
        "severity": "High",
        "color": "Yellow",
        "meaning": "Power steering assistance may be reduced or lost.",
        "action": "Grip steering wheel firmly. Avoid high speed. Visit mechanic immediately.",
        "category": "Steering"
    },
    "Steering": {
        "severity": "High",
        "color": "Yellow",
        "meaning": "General steering system warning detected.",
        "action": "Drive carefully. Avoid sharp turns. Visit mechanic as soon as possible.",
        "category": "Steering"
    },

    # ── STABILITY / TRACTION ──────────────────────────────────
    "Electronic Stability Problem -ESP-": {
        "severity": "High",
        "color": "Yellow",
        "meaning": "Electronic stability program fault detected.",
        "action": "Drive carefully on slippery roads. Vehicle stability control is reduced. Visit mechanic.",
        "category": "Stability"
    },
    "Electronic stability programme": {
        "severity": "High",
        "color": "Yellow",
        "meaning": "ESP system fault. Vehicle may be less stable during cornering or on wet roads.",
        "action": "Reduce speed. Avoid sudden steering. Visit mechanic soon.",
        "category": "Stability"
    },

    # ── LANE / DRIVING ASSIST ─────────────────────────────────
    "Lane Departure": {
        "severity": "Medium",
        "color": "Yellow",
        "meaning": "Vehicle is drifting out of its lane without signaling.",
        "action": "Hold steering wheel firmly. Stay within lane markings.",
        "category": "Driver Assist"
    },
    "LaneCenteringOff": {
        "severity": "Low",
        "color": "White",
        "meaning": "Lane centering assist feature has been turned off.",
        "action": "No immediate action needed. Enable lane centering if desired.",
        "category": "Driver Assist"
    },

    # ── DOORS ─────────────────────────────────────────────────
    "Door open": {
        "severity": "Medium",
        "color": "Red",
        "meaning": "One or more doors are not fully closed.",
        "action": "Stop safely and ensure all doors are properly shut before driving.",
        "category": "Doors"
    },
    "Doors": {
        "severity": "Medium",
        "color": "Red",
        "meaning": "A door is ajar or not properly latched.",
        "action": "Check all doors including boot/trunk. Close firmly before driving.",
        "category": "Doors"
    },

    # ── LIGHTS ────────────────────────────────────────────────
    "FrontFogLight": {
        "severity": "Low",
        "color": "Green",
        "meaning": "Front fog lights are currently switched on.",
        "action": "No action needed. Turn off when fog clears to avoid blinding other drivers.",
        "category": "Lights"
    },
    "Low beam": {
        "severity": "Low",
        "color": "Green",
        "meaning": "Low beam headlights are currently active.",
        "action": "No action needed. This is a status indicator.",
        "category": "Lights"
    },
    "SideLamp": {
        "severity": "Low",
        "color": "Green",
        "meaning": "Side lamps / parking lights are switched on.",
        "action": "No action needed unless lights were left on accidentally.",
        "category": "Lights"
    },

    # ── OTHER WARNINGS ────────────────────────────────────────
    "Central Warning lamp": {
        "severity": "High",
        "color": "Red",
        "meaning": "Central warning system has detected a general vehicle fault.",
        "action": "Check other warning lights. Visit mechanic for full diagnosis.",
        "category": "General"
    },
    "Master Warning": {
        "severity": "High",
        "color": "Yellow",
        "meaning": "Multiple systems have triggered a warning. Check vehicle information display.",
        "action": "Read the vehicle display message. Visit mechanic for full system check.",
        "category": "General"
    },
    "Washer Fluid": {
        "severity": "Low",
        "color": "Yellow",
        "meaning": "Windscreen washer fluid level is low.",
        "action": "Refill washer fluid reservoir with appropriate fluid.",
        "category": "Maintenance"
    },
    "security": {
        "severity": "Medium",
        "color": "Red",
        "meaning": "Vehicle security or immobilizer system warning.",
        "action": "Check if correct key is being used. Visit mechanic if problem persists.",
        "category": "Security"
    },
}


# =============================================================
# Helper Functions
# =============================================================

def get_light_details(class_name: str) -> dict:
    """
    Get warning light details by class name.
    Returns default if class not found.
    """
    return WARNING_LIGHT_INFO.get(class_name, {
        "severity": "Unknown",
        "color": "Unknown",
        "meaning": "An unrecognized warning light was detected.",
        "action": "Consult your vehicle manual or visit a mechanic for diagnosis.",
        "category": "Unknown"
    })


def get_severity_level(severity: str) -> int:
    """
    Convert severity string to numeric level for sorting.
    Higher number = more urgent.
    """
    levels = {
        "Critical": 4,
        "High":     3,
        "Medium":   2,
        "Low":      1,
        "Unknown":  0
    }
    return levels.get(severity, 0)


def sort_by_severity(detections: list) -> list:
    """
    Sort list of detections by severity (most critical first).
    """
    return sorted(
        detections,
        key=lambda x: get_severity_level(x.get("severity", "Unknown")),
        reverse=True
    )


def get_all_classes() -> list:
    """Return all class names in the database."""
    return list(WARNING_LIGHT_INFO.keys())


def get_classes_by_category(category: str) -> list:
    """Return all warning lights in a specific category."""
    return [
        name for name, info in WARNING_LIGHT_INFO.items()
        if info["category"] == category
    ]


# =============================================================
# Quick Test
# =============================================================
if __name__ == "__main__":
    print("=== All Warning Light Classes ===")
    for i, name in enumerate(get_all_classes()):
        info = get_light_details(name)
        print(f"{i+1:02d}. [{info['severity']:8}] {name}")

    print(f"\nTotal classes: {len(WARNING_LIGHT_INFO)}")

    print("\n=== Test: Check Engine ===")
    print(get_light_details("Check Engine"))

    print("\n=== Test: Unknown Light ===")
    print(get_light_details("Something Random"))
