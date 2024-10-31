#[derive(Debug, Default, GoGenerate)]
struct ServiceInfoGroup {
    operator_ref: Option<String>,         // OperatorCode
    product_category_ref: Option<String>, // ProductCategoryCode
    service_feature_ref: Vec<String>,     // Vec<ServiceFeatureCode>
    vehicle_feature_ref: Vec<String>,     // Vec<VehicleFeatureCode>
}
