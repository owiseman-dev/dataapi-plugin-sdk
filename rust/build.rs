fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("cargo:rerun-if-changed=../src/main/proto/plugin_service.proto");
    
    tonic_build::compile_protos("../src/main/proto/plugin_service.proto")?;
    
    Ok(())
}