use go_generation_derive::GoGenerate;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, GoGenerate)]
pub struct Line {
    line_direction: String,
    line_ref: String,
}
