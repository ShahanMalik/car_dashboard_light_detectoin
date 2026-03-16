Quick description
- Detects dashboard warning lights in a single image and shows simple explanations and actions.



4. Run the script:
   - python roboflow_test.py


What the script does (simple flow)
- Sends `original.jpg` to a Roboflow model.
- Receives detected labels and confidence scores.
- Looks up each label in `warning_info.py` for severity, meaning, and action.
- Prints results sorted by severity.
