import Foundation
import Vision
import CoreImage
import AppKit

/// Person cutout via Vision foreground-instance masking.
/// usage: cutout <in.png> <out.png>   (out is RGBA PNG, background removed)
let args = CommandLine.arguments
guard args.count == 3, let img = CIImage(contentsOf: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("usage: cutout <in.png> <out.png>\n".data(using: .utf8)!)
    exit(2)
}

let request = VNGenerateForegroundInstanceMaskRequest()
let handler = VNImageRequestHandler(ciImage: img)
try handler.perform([request])
guard let result = request.results?.first else {
    FileHandle.standardError.write("no foreground found\n".data(using: .utf8)!)
    exit(1)
}
let maskPB = try result.generateScaledMaskForImage(forInstances: result.allInstances, from: handler)
let mask = CIImage(cvPixelBuffer: maskPB)

let blend = CIFilter(name: "CIBlendWithMask", parameters: [
    kCIInputImageKey: img,
    kCIInputBackgroundImageKey: CIImage.empty(),
    kCIInputMaskImageKey: mask,
])!
let out = blend.outputImage!.cropped(to: img.extent)

let ctx = CIContext()
guard let cg = ctx.createCGImage(out, from: img.extent) else { exit(1) }
let rep = NSBitmapImageRep(cgImage: cg)
try rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: args[2]))
