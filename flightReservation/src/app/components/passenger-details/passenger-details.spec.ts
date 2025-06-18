import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PassengerDetails } from './passenger-details';

describe('PassengerDetails', () => {
  let component: PassengerDetails;
  let fixture: ComponentFixture<PassengerDetails>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PassengerDetails]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PassengerDetails);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
