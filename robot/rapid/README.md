# ABB RAPID programs

Owner: **Cristhian Guerreño** · Documentation: [03 · Robot calibration](../../docs/03_robot_calibration.md)

Put RAPID modules (`.mod`, `.modx`, `.sys`) exported from RobotStudio in this folder. Every module needs a header comment with its purpose, its author and whether it has been tested in simulation and/or on the real robot.

## Historical reference: `TCPServer` sample (not in repo yet)

An earlier RAPID sample was reviewed. It is **not a validated program**. Check the robot limits, configuration, network and controller options before reusing it.

- `MODULE TCPServer`: socket server (`socketdev` server/client) on the controller, listening on port 5000.
- `MoveStep`: reads the current joints with `CJointT()` and increments or decrements **joint 6** in 10° steps. `j6_curr` starts at −180.
- Robtargets mentioned: `gripper_extend`, `wire`, `wireTocamera`, `camera_50mm`.



## Conventions
- Use workobjects and tooldata, never targets referenced only to the base frame.
- Use speed data that is safe for testing (reduced speed) and document it.
- Test in RobotStudio simulation before running on the physical robot.
