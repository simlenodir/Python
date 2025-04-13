from datetime import datetime

# Starting Blog program 
# Starting with Bismilah

class Posts:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestemp = datetime.now()

    def __str__(self):
        return f"\nTitle: {self.title} \nAuthor: {self.author} \nTime: {self.timestemp}\nContent: {self.content}"
    
class Blog:
    def __init__(self):
        self.posts = []

    # 1 Adding post to list
    def add_post(self):
        title = input("Enter title: ")
        content = input("Enter content: ")
        author = input("Enter author: ")
        # Checking Posts lists is empty
        if len(self.posts) == 0:
            new_post = Posts(title, content, author)
            if new_post:
                self.posts.append(new_post)
                print("Post added.")
            else:
                print('Something is wrong check your inputs')
        else:
            new_post = Posts(title, content, author)
            if new_post:
                self.posts.append(new_post)
                print("Post added.")
            else:
                print('Something is wrong check your inputs')

    # 2 Showing all posts
    def all_posts(self):
        if len(self.posts) == 0:
            print("Posts list is empty. Would you like create post ?")
            choice = input('Enter Your Choice yes/no: ')
            if choice.lower() == 'yes':
                self.add_post()
            else: 
                print("We will be happy if you choice yes")
        else:
            for post in self.posts:
                print(post)

    # 3 Display Post by Author
    def find_by_author(self, author):
        # Checking if list is empty
        if len(self.posts) == 0:
            print("Posts list is empty")
        else:
            found_post = next((post for post in self.posts if post.author.lower() == author.lower()), None)
            if found_post:
                print(f'Post by this {author}: {found_post}')
    # 4 Delete post
    def delete_post(self, title):
        if len(self.posts) == 0:
            print("Posts List is empty")
        else:
            for i, post in enumerate(self.posts):
                if post.title == title:
                    del self.posts[i] 
                    print(f'{title} post is deleted')
                    return
            print(f"No post found with title '{title}'.")
    
    # 5 Edit Post
    def edit_post(self, title, new_title=None, new_content = None):
        if len(self.posts) == 0:
            print("Posts lists is empty")
        else:
            found_post = next((post for post in self.posts if post.title.lower() == title.lower()), None)
            if found_post:
                    if new_title:
                        found_post.title = new_title
                    elif new_content:
                        found_post.content = new_content
            else:
                print('Post not found')
                    
    # 6 Latest Posts
    def latest_posts(self, count):
        if len(self.posts) == 0:
            print("Posts lists is empty")
        else:
            lates_posts = sorted(self.posts, key = lambda p: p.timestemp, reverse = True)
            print(f"Displaying latest {count} post(s):")
            for post in lates_posts[:count]: 
                print(post)


def main():
    blog = Blog()

    while True:
        print("\n--- Blog System Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1': 
            blog.add_post()
        elif choice == '2':
            blog.all_posts()
        elif choice == '3':
            author = input('Enter Your author: ')
            blog.find_by_author(author)
        elif choice == '4':
            title = input('Enter Your title: ')
            blog.delete_post(title)
        elif choice == '5':
            title = input('Enter Your title: ')
            new_title = input('Edit new post title: ')
            new_content = input('Enter your new content: ')
            blog.edit_post(title, new_title or None, new_content or None)
        elif choice == '6':
            count = input("How many latest posts display ? default 3: ")
            blog.latest_posts(int(count) if count.isdigit() else 3)

        elif choice == '7':
            print("Exiting Blog System.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()