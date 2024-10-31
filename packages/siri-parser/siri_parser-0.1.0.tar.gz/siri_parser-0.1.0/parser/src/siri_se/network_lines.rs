use serde::{Deserialize, Serialize};


#[derive(Debug, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "camelCase")]
pub struct AffectedStopPoint {
    pub stop: Option<StopPointRef>,             // Reference to the impacted scheduled stop point
    pub modes: Option<AffectedModes>,            // Modes impacted at the stop point
    pub zone: Option<PlaceRef>,                  // Reference to the zone where the stop point is located
    pub place_name: Vec<String>,                 // Names of the places where the scheduled stop point is located
    pub accessibility_assessment: Option<AccessibilityAssessment>, // Accessibility assessment for the stop point
    pub stop_condition: Vec<RoutePointType>,     // Conditions of the scheduled stop point
    pub connection_links: Option<Vec<AffectedConnectionLink>>, // Affected connection links at the stop point
}