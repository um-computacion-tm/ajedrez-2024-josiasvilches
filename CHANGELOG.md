# Changelog



## [0.045] - 2024-10-20

### Fixed

- Issues with excessive arguments (CodeClimate).



## [0.044] - 2024-10-19

### Changed

- Functions redistributed and moved to other files: 

  - `movements.py`

  - `chess.py`

  

### Added

- New file: `utils.py` (contains auxiliary functions).



## [0.043] - 2024-10-18

### Fixed

- Corrections for CodeClimate improvements.



## [0.042] - 2024-10-17

### Changed

- Improved pawn movement; movements enabled.



## [0.041] - 2024-10-16

### Fixed

- Code corrections to improve CodeClimate rating; pawn movements disabled.



## [0.040] - 2024-10-15

### Changed

- Removed free will from all pieces; pieces now respect the one in front. 

- Added a message when a piece captures another.



## [0.039] - 2024-10-14

### Changed

- Removed free will from pieces; moved functions to their corresponding files; turn change disabled.



## [0.038] - 2024-10-13

### Fixed

- Corrections to the move validator.



## [0.037] - 2024-10-12

### Fixed

- Corrections to pawn movements.



## [0.036] - 2024-10-11

### Changed

- Modification to pawn movement.



## [0.035] - 2024-10-10

### Changed

- Adjusted functions; movements enabled; gameplay errors in some pieces fixed.



## [0.034] - 2024-10-09

### Changed

- Modification to `movements.py` for code quality improvement; movements still disabled.



## [0.033] - 2024-10-08

### Changed

- The board is displayed again; movements still not possible.



## [0.032] - 2024-10-07

### Changed

- Attempted to display the board with the changes in the `movements.py` file.



## [0.031] - 2024-10-04

### Fixed

- Corrections applied to diagonal movement in the `movements.py` file.



## [0.030] - 2024-10-03

### Changed

- Major restructuring to improve CodeClimate rating; added `movements.py` to consolidate all possible movements of each piece; the program is currently non-functional.



## [0.029] - 2024-10-02

### Added

- Tests for the bishop.



## [0.028] - 2024-10-01

### Added

- Created tests for the pawn.



## [0.027] - 2024-09-27

### Removed

- Deleted `venv` folder.



## [0.026] - 2024-09-26

### Fixed

- Pieces can finally move.



## [0.025] - 2024-09-25

### Fixed

- Improved piece visibility; pieces now appear in white and black on the board.



## [0.024] - 2024-09-24

### Changed

- Renamed `start_position` to `from_position` for all relevant movements.



## [0.023] - 2024-09-23

### Changed

- Changed letters to pieces for faster identification of whose turn it is and simplified the assignment of colors to each piece.



## [0.022] - 2024-09-22

### Added

- The board now displays letters.



## [0.021] - 2024-09-21

### Attempted

- Attempted to display the board during execution of `cli.py`.



## [0.020] - 2024-09-20

### Added

- Integrated exceptions into the `chess` file.



## [0.019] - 2024-09-19

### Added

- Added an exceptions file; integrated exceptions in `board`, and the game can now start using `cli.py`.



## [0.018] - 2024-09-18

### Changed

- Improved board logic; added piece movement validation and possible outcomes (empty space, piece of another color, and piece of the same color).



## [0.017] - 2024-09-17

### Changed

- Improvements made to the board.



## [0.016] - 2024-09-09

### Changed

- Improved knight movement.



## [0.015] - 2024-09-08

### Added

- Added logic for knight movement.



## [0.014] - 2024-09-05

### Changed

- Improved queen logic.



## [0.013] - 2024-09-03

### Added

- Added initial logic for queen piece.



## [0.012] - 2024-09-02

### Changed

- Improved knight logic.



## [0.011] - 2024-08-29

### Added

- Added initial logic for knight movement.



## [0.010] - 2024-08-28

### Added

- Added initial logic for king movement.



## [0.009] - 2024-08-27

### Added

- Added missing pieces to the board and started implementing rook logic.



## [0.008] - 2024-08-26

### Added

- Created files for each piece.



## [0.007] - 2024-08-23

### Added

- Pawn movements added to the code.



## [0.006] - 2024-08-20

### Fixed

- Reconfigured the virtual environment; tests can now run from different folders.



## [0.005] - 2024-08-19

### Added

- Implemented part of the pawn logic; improved piece class logic, and created tests for the board.



## [0.004] - 2024-08-16

### Added

- Added bishops and knights pieces.



## [0.003] - 2024-08-15

### Added

- Uploaded files provided by the instructor to guide the class.



## [0.002] - 2024-08-13

### Updated

- Updated markdown files (README and CHANGELOG).



## [0.001] - 2024-08-11

### Added

- Initial version; set up the environment for the program.
