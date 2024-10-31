

#[derive(Debug, Default)]
struct DistributorDepartureCancellation {
    recorded_at_time: String, // Date et heure de production des données
    distributor_info: DistributorInfoGroup, // Informations sur le distributeur
    reason: String, // Raison de l'annulation
    extension: Option<String>, // Emplacement pour extension utilisateur
}