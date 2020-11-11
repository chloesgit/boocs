import { Author } from './author';

export interface Book {
  id: number;
  nom: string;
  description?: string;
  content: string;
  active: boolean;
  author: Author;
  year: number;
}
