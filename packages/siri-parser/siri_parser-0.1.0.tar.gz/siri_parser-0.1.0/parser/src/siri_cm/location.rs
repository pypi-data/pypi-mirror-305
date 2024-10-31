


struct LocationStructure {
    id: Option<String>, // Identifiant du point pour un lien avec une base Géospatiale
    srs_name: Option<String>, // Identifiant du référentiel de projection
    coordinates: Option<Coordinates>, // Localisation en WGS 84 ou autre référentiel
    precision: Option<f64>, // Précision du positionnement en mètres
}