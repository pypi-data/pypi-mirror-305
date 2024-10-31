use serde::{Deserialize, Serialize};

use crate::{models::framed_vehicle_journey_ref::FramedVehicleJourneyRef, siri_et::distribution_group::DisruptionGroup, siri_sm::{journey_pattern_info_group::JourneyPatternInfoGroup, vehicle_journey_info_group::VehicleJourneyInfoGroup}};


#[derive(Debug, Default, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "PascalCase")]
struct FeederJourney {
    vehicle_journey_identity: LineCode, // Identifiant de la ligne
    direction_ref: DirectionCode, // Indication de direction (aller/retour)
    framed_vehicle_journey_ref: Option<FramedVehicleJourneyRef>, // Identification de la course
    journey_pattern_info: Option<JourneyPatternInfoGroup>, // Info sur le schéma de mission
    vehicle_journey_info: Option<VehicleJourneyInfoGroup>, // Info sur la course
    disruption_group: Option<DisruptionGroup>, // Infos sur les perturbations
    progress: Option<bool>, // Indique si l’information temps réel est disponible
    aimed_arrival_time: Option<String>, // Heure d’arrivée prévue à l’arrêt
    //extensions: Option<Extensions>, // Optional user-defined extensions
}