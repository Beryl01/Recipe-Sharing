import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FilterFtComponent } from './filter-ft.component';

describe('FilterFtComponent', () => {
  let component: FilterFtComponent;
  let fixture: ComponentFixture<FilterFtComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FilterFtComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FilterFtComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
