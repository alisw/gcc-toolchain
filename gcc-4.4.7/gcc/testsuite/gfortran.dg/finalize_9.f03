! { dg-do compile }

! Parsing of finalizer procedure definitions.
! While ALLOCATABLE scalars are not implemented, this even used to ICE.
! Thanks Tobias Burnus for the test!

integer, allocatable :: x ! { dg-error "may not be ALLOCATABLE" }
end
