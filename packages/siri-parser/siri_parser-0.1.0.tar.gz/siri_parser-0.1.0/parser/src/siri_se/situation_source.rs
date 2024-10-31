use serde::{Serialize, Deserialize};

#[derive(Debug)]
struct SituationSource {
    country: Option<String>, // Pays d’origine de la Source (Code IANA)
    source_type: SourceType, // Nature de la source
    details: Option<SituationSourceDetails>, // Détails supplémentaires sur la source
}