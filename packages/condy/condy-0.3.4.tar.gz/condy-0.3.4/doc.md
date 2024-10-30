# SAM2 API Documentation

This document provides information about the endpoints available in the SAM2 (Segment Anything Model 2) API, formatted for easy use with Postman.

## Base URL

```
https://your-api-base-url.com
```

Replace `your-api-base-url.com` with the actual base URL of your deployed API.

## Endpoints

### 1. Single Segmentation

Generates a single mask for the input image based on the provided points.

- **Method**: POST
- **Endpoint**: `/segment/single`
- **Body**: form-data

```json
{
  "file": "(binary file)",
  "points": "[[200, 200], [300, 300]]",
  "labels": "[1, 0]"
}
```

Note: In Postman, set `file` to type "File" and select your image file.

### 2. All Segmentations

Generates all possible masks for the input image based on the provided points.

- **Method**: POST
- **Endpoint**: `/segment/all`
- **Body**: form-data

```json
{
  "file": "(binary file)",
  "points": "[[200, 200], [300, 300]]",
  "labels": "[1, 0]"
}
```

Note: In Postman, set `file` to type "File" and select your image file.

### 3. Box Segmentation

Generates a mask for the input image based on the provided bounding box.

- **Method**: POST
- **Endpoint**: `/segment/box`
- **Body**: form-data

```json
{
  "file": "(binary file)",
  "box": "[10, 10, 100, 100]"
}
```

Note: In Postman, set `file` to type "File" and select your image file.

### 4. Custom Output Segmentation

Generates a custom output based on the segmentation and the specified parameters.

- **Method**: POST
- **Endpoint**: `/segment/custom`
- **Body**: form-data
- **Query Params**: Add these in the "Params" tab in Postman

```json
{
  "file": "(binary file)",
  "points": "[[200, 200], [300, 300]]",
  "labels": "[1, 0]",
  "flag": "0"
}
```

Query Params:
```json
{
  "compression": "performance",
  "output_format": "png"
}
```

Note: In Postman, set `file` to type "File" and select your image file.

#### Parameters for Custom Output:

- `flag`: 
  - 0: Segmented object with transparent background
  - 1: Inverse of the segmentation with transparent background
  - 2: Black and white mask
- `compression`: 
  - "quality": High quality, slower compression
  - "performance": Balanced quality and speed
  - "fast": Faster compression, lower quality
- `output_format`: 
  - "png": PNG format
  - "webp": WebP format
  - "jpeg": JPEG format

## Notes

- All endpoints return image data directly.
- For endpoints that accept points and labels, these are optional. If not provided, a default point at the center of the image will be used.
- The API uses SAM2 (Segment Anything Model 2) for image segmentation, providing state-of-the-art results for interactive segmentation tasks.