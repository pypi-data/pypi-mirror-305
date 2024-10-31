use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
pub enum VerificationStatus {
    Unknown,
    Unverified,
    Verified,
}
