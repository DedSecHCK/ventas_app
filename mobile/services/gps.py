try:
    from plyer import gps
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False
    print("Warning: plyer not available, using mock GPS data")

def get_location():
    """Get current GPS location"""
    if PLYER_AVAILABLE:
        try:
            # Configure GPS
            gps.configure(on_location=on_location_update, on_status=on_status_update)
            gps.start(minTime=1000, minDistance=0)
            
            # In a real app, this would wait for GPS callback
            # For now, return default location
            return {"lat": 0.0, "lon": 0.0}
        except Exception as e:
            print(f"Error getting GPS location: {e}")
            return {"lat": 0.0, "lon": 0.0}
    else:
        # Return mock location for testing
        return {"lat": 4.6097, "lon": -74.0817}  # Bogotá, Colombia

def on_location_update(**kwargs):
    """Callback when GPS location is updated"""
    lat = kwargs.get('lat', 0.0)
    lon = kwargs.get('lon', 0.0)
    print(f"GPS Location updated: {lat}, {lon}")
    return {"lat": lat, "lon": lon}

def on_status_update(stype, status):
    """Callback when GPS status changes"""
    print(f"GPS Status: {stype} - {status}")

def stop_gps():
    """Stop GPS tracking"""
    if PLYER_AVAILABLE:
        try:
            gps.stop()
        except Exception as e:
            print(f"Error stopping GPS: {e}")