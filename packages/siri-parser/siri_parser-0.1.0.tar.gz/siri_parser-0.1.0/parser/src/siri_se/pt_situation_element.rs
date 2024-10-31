use serde::{Deserialize, Serialize};


#[derive(Debug, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "PascalCase")]
pub struct PtSituationElement {
    creation_time: String, // Heure de creation de SITUATION (xsd:dateTime)
    situation_based_identity_group: SituationSharedIdentityGroup, // Référence à une SITUATION
    country_ref: Option<String>, // Code Pays du participant
    participant_ref: Option<String>, // Identifiant du système participant
    situation_number: Option<String>, // Identifiant unique d’une SITUATION pour un Participant
    situation_update_identity: Option<SituationUpdateIdentityGroup>, // Référence pour mise à jour
    situation_info: Option<SituationSource>, // Source d’une SITUATION
    versioned_at_time: Option<String>, // Date/heure de versionnement
    verification: Option<VerificationStatus>, // Indique si la SITUATION a été vérifiée
    progress: Option<ProgressStatus>, // État de SITUATION
    quality_index: Option<QualityIndex>, // Évaluation de l'exactitude des données
    publication: Option<Vec<PublicationStatus>>, // Statut de publication
    validity_period: Vec<ValidityPeriod>, // Période d'application globale
    publication_window: Option<Vec<PublicationWindow>>, // Fenêtre de publication
    reason: String, // Raison de la situation
    severity: Option<Severity>, // Sévérité de SITUATION
    priority: Option<u32>, // Classement de priorité
    sensitivity: Option<Sensitivity>, // Confidentialité de SITUATION
    audience: Option<Audience>, // Audience de SITUATION
    scope_type: Option<String>, // Type de périmètre de SITUATION
    planned: bool, // Indique si la SITUATION était planifiée
    keywords: Option<Vec<String>>, // Mots-clés de la SITUATION
    summary: Option<String>, // Résumé de la SITUATION
    description: Option<String>, // Description de la SITUATION
    detail: Option<String>, // Détails supplémentaires
    advice: Option<String>, // Autres conseils aux passagers
    internal: Option<String>, // Description interne
    images: Option<Vec<Image>>, // Images associées
    info_links: Option<Vec<InfoLink>>, // Liens d'informations
    affects: Option<Affects>, // Parties du réseau affectées
    consequences: Option<Vec<Consequence>>, // Conséquences de l'événement
    publishing_actions: Option<Actions>, // Conséquence d’une SITUATION
}