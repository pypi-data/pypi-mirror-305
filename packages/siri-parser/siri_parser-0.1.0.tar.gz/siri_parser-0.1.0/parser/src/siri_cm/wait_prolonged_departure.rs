

#[derive(Debug)]
struct WaitProlongedDeparture {
    recorded_at_time: DateTime<Utc>, // Date et heure des données
    distributor_info: DistributorInfoGroup, // Information du distributeur
    expected_departure_time: DateTime<Utc>, // Nouvelle heure de départ prévue
    extensions: Option<Extensions>, // Emplacement pour extension utilisateur
}