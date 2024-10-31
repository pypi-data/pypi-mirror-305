use go_generation_derive::GoGenerate;
use pyo3::pyclass;
use serde::{Deserialize, Serialize};

use crate::SiriServiceType;

#[pyclass]
#[derive(Debug, PartialEq, Deserialize, Serialize, Eq)]
pub struct Body(pub SiriServiceType);
