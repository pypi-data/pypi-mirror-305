

#[derive(Debug)]
pub struct Affects {
    pub level: Option<AreaOfInterest>,      // Geographic area of interest
    pub operators: Option<Operators>,        // Operators affected
    pub network: Option<Networks>,           // Networks impacted
    pub stop: Option<StopPoints>,            // Scheduled stop points impacted
    pub stop_place: Option<StopPlaces>,      // Stop places impacted
    pub place: Option<Places>,                // Places impacted
    pub journey: Option<VehicleJourneys>,    // Vehicle journeys impacted
    pub vehicles: Option<Vehicles>,           // Vehicles impacted
}