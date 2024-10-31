use serde::{Deserialize, Serialize};




#[derive(Debug, Default, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "PascalCase")]
pub struct MonitoredFeederArrival {
    recorded_at_time: String, // Date and time data was produced
    identity: Option<ItemIdentifier>, // Reference to the information message
    interchange_ref: Option<String>, // Identifiant de la correspondance entre course
    connection_link_ref: String, // Identifiant de la correspondance physique
    stop_point_ref: Option<String>, // Identifiant du point d’arrêt de l’amenant
    order: Option<u32>, // Numéro d'ordre de l'arrêt dans la mission
    stop_point_name: Option<String>, // Nom du point d'arrêt
    clear_down_ref: Option<String>, // Indicateur « véhicule à l’arrêt » ou « à l’approche »
    journey_info: FeederJourney, // Description de la course de l’amenant
    vehicle_at_stop: Option<bool>, // Indicateur "Véhicule à l’arrêt"
    aimed_arrival_time: Option<String>, // Heure d'arrivée planifiée
    expected_arrival_time: String, // Heure d’arrivée prévue à l’arrêt
    arrival_platform_name: Option<String>, // Nom du quai d'arrivée
   // extensions: Option<Extensions>, // Optional user-defined extensions
}