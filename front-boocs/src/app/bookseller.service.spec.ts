import { TestBed } from '@angular/core/testing';

import { BooksellerService } from './bookseller.service';

describe('BooksellerService', () => {
  let service: BooksellerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BooksellerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
