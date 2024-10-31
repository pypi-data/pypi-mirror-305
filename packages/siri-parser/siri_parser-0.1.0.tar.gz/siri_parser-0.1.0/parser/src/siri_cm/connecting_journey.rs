use serde::{Deserialize, Serialize};

#[derive(Debug, Default, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
struct ConnectingJourney {
    line_ref: Option<String>, // Identifiant de la ligne
    framed_vehicle_journey_ref: Option<FramedVehicleJourneyRef>, // Identifiant de la course
    journey_pattern_info: Option<JourneyPatternInfoGroup>, // Information sur le parcours
    vehicle_journey_info: Option<VehicleJourneyInfoGroup>, // Information sur la course
    disruption_group: Option<DisruptionGroup>, // Information sur les perturbations
    progress: Option<bool>,   // Indique si les données temps réel sont disponibles
    aimed_arrival_time: Option<String>, // Heure d’arrivée prévue à la correspondance
    extensions: Option<Vec<String>>, // Emplacement pour extension utilisateur
}
