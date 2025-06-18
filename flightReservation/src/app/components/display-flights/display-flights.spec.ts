import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayFlights } from './display-flights';

describe('DisplayFlights', () => {
  let component: DisplayFlights;
  let fixture: ComponentFixture<DisplayFlights>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplayFlights]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisplayFlights);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
