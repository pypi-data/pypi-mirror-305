

#[derive(Debug, Default)]
struct StoppingPositionChangedDeparture {
    recorded_at_time: chrono::DateTime<chrono::Utc>, // Date et heure de production des données
    distributor_info: DistributorInfoGroup, // Informations sur le distributeur
    change_note: String, // Description de la nouvelle position
    new_location: Option<Location>, // Nouvelle position de l’arrêt
}