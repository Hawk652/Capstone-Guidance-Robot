# Analysis of the Localization System

## Localization Subsystem

The specification that will be tested is:

- Shall detect the AuR's position to a precision of 15cm  

### Testing Method

Since the originally decided UWB boards did not arrive in time, we decided to explore the possibility of bluetooth based positioning. We used two ESP32s for this test, one as a beacon and one as a reciever. Below is an account of the measurements and calculations used to test accuracy. We tested only distance error since positional error relies entirely on distancing error. 

### Data

Each RSSI shown below is an average of 5 samples. Distance estimate is 

$$10^{\frac{Measured RSSI - InstantRSSI}{10N}}$$

[1] N is the natural constant which for which we use 4. The measured RSSI is the RSSI at 1 meter.

 #### RSSI at 1.00 meters
| RSSI: 1.00m |
| ---- |
| \-43 |
| \-42 |
| \-42 |
| \-43 |
| \-42 |
| \-42 |
| \-43 |
| \-43 |
| \-43 |  

Measured RSSI = -42.55555556

  

#### RSSI at 0.75 meters

| RSSI: 0.75m | estimate(m) |
| ----------- | ----------- |
| \-45 | 1.151094851 |
| \-47 | 1.291549665 |
| \-48 | 1.368078794 |
| \-48 | 1.368078794 |
| \-47 | 1.291549665 |
| \-48 | 1.368078794 |
| \-49 | 1.449142559 |
| \-49 | 1.449142559 |
| \-50 | 1.535009654 |
| Average: | 1.363525037 |
| Error: | 0.613525037 |  

#### RSSI at 0.5 meters

| RSSI: 0.5m | estimate(m) |
| ---------- | ----------- |
| \-41 | 0.914347141 |
| \-42 | 0.968525615 |
| \-41 | 0.914347141 |
| \-41 | 0.914347141 |
| \-41 | 0.914347141 |
| \-40 | 0.863199363 |
| \-41 | 0.914347141 |
| \-41 | 0.914347141 |
| \-41 | 0.914347141 |
| Average: | 0.914683885 |
| Error: | 0.414683885 |  

#### RSSI at 0.25 meters

| RSSI: 0.25m | estimate(m) |
| ----------- | ----------- |
| \-37 | 0.72629175 |
| \-37 | 0.72629175 |
| \-37 | 0.72629175 |
| \-38 | 0.769327242 |
| \-38 | 0.769327242 |
| \-37 | 0.72629175 |
| \-37 | 0.72629175 |
| \-38 | 0.769327242 |
| \-37 | 0.72629175 |
| Average: | 0.740636914 |
| Error: | 0.490636914 |

#### RSSI at 2 meters

| RSSI: 2m | estimate(m) |
| -------- | ----------- |
| \-41 | 0.914347141 |
| \-39 | 0.814912747 |
| \-38 | 0.769327242 |
| \-38 | 0.769327242 |
| \-38 | 0.769327242 |
| \-38 | 0.769327242 |
| \-37 | 0.72629175 |
| \-37 | 0.72629175 |
| \-35 | 0.647308204 |
| Average: | 0.767384507 |
| Error: | 1.232615493 |

### Results

The errors presented are far too great to fit our constraint and are far too varied to correct. The positional error of trilateration is estimated to be greater than the distancing error. Our positional error constraint is under 15cm while our maximum error is above 1.2m. This is not a viable option.

## Sources

[1] R. Shah, “Convert RSSI Value of the BLE (Bluetooth Low Energy) Beacons to Meters,” BeingCoders, Jul. 26, 2021. https://medium.com/beingcoders/convert-rssi-value-of-the-ble-bluetooth-low-energy-beacons-to-meters-63259f307283
