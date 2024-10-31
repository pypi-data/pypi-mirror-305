


#[derive(Debug)]
pub struct PublishAtScope {
    pub scope_type: Option<ScopeType>,             // Optional type of the action
    pub affects: Option<Affects>,                   // Optional area affected by the action
}