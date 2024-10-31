use serde::{Deserialize, Serialize};


#[derive(Debug, Default, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "PascalCase")]
pub struct MonitoredFeederArrivalCancellation {
    recorded_at_time: String, // Date et heure des données
    identity: Option<ItemIdentifier>, // Identifie l’objet annulé
    interchange_ref: Option<InterchangeCode>, // Identifiant de la correspondance entre courses
    connection_link_ref: ConnectionLinkCode, // Identifiant de la correspondance physique
    stop_point_ref: Option<StopPointCode>, // Identifiant du point d’arrêt
    order: Option<u32>, // Numéro d'ordre de l'arrêt dans la mission
    stop_point_name: Option<String>, // Nom du point d'arrêt
    journey_info: JourneyInfo, // Info sur la course
    info_reason: Option<String>, // Cause de l’annulation
    extensions: Option<Extensions>, // Emplacement pour extension utilisateur
}