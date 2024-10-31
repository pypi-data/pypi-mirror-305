

#[derive(Debug, Default)]
struct DistributorInfoGroup {
    interchange_ref: Option<String>, // Identifiant de la correspondance entre courses
    connection_link_ref: String, // Identifiant de la correspondance physique
    stop_point_ref: Option<String>, // Identifiant du point d'arrêt du partant
    distributor_order: Option<u32>, // Numéro d'ordre de l'arrêt dans la mission
    distributor_journey: ConnectingJourneyStructure, // Description de la course du véhicule au départ
    feeder_vehicle_journey_ref: Option<Vec<FramedVehicleJourneyRefStructure>>, // Informations sur la course de l’amenant
}