import Foundation
import Vision
import CoreImage

/// Face rectangles via Vision. usage: facex <in.png> -> one "cx cy w h" line per face in pixels.
let args = CommandLine.arguments
guard args.count == 2, let img = CIImage(contentsOf: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("usage: facex <in.png>\n".data(using: .utf8)!)
    exit(2)
}
let request = VNDetectFaceRectanglesRequest()
let handler = VNImageRequestHandler(ciImage: img)
try handler.perform([request])
let W = img.extent.width, H = img.extent.height
for f in request.results ?? [] {
    let b = f.boundingBox
    print(String(format: "%.0f %.0f %.0f %.0f", (b.midX) * W, (1 - b.midY) * H, b.width * W, b.height * H))
}
