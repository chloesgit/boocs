import { Component, OnInit } from '@angular/core';
import { BooksellerService } from '../bookseller.service';
import { Book } from '../types/book';

@Component({
  selector: 'app-library',
  templateUrl: './library.component.html',
  styleUrls: ['./library.component.scss'],
})
export class LibraryComponent implements OnInit {
  private books: Book[];
  constructor(private bookseller: BooksellerService) {}

  ngOnInit(): void {
    this.bookseller.getBooks().subscribe((books) => (this.books = books));
  }

  public get getBooks(): Book[] {
    return this.books;
  }
}
