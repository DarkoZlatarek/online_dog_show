# [**Online Dog Show**](#online-dog-show)
Online dog show is a page where users can post the photo of their dog/s and see other people's photos of dogs. Users can like other posts. Interacting with each other is possible through comments on their posts. There is a little harmless competition between users. The most liked photo is displayed on its own. There is no reward apart from ego boost.


## [Table of content](#table-of-content)
* [User experience](#user-experience)
    * [Site purpose](#site-purpose)
    * [Site goal](#site-goal)
    * [Target audience](#target-audience)
    * [User goals](#user-goals)
    * [Future goals](#future-goals)
* [User stories](#user-stories)
    * [Admin stories](#admin-stories)
    * [User stories](#user-stories)
* [Design](#design)
    * [Wireframe](#wireframe)
    * [Database schema](#database-schema)
    * [Color schema](#color-schema)
    * [Typography](#typography)
    * [Imagery](#imagery)
* [Features](#features)
    * [Existing features](#existing-features)
    * [C.R.U.D.](#crud)
    * [Future features](#future-features)
* [Testing](#testing)


<hr>

## **User experience (UX)**<span id="user-experience"><span>
<br>

### **Site purpose**
The intent of the Online Dog Show site is to bring dog owners together. It is a place where they can safely post the photo of their bellowed dog with a short description/story about the photo. Users of the site are able to discuss about the dog breed and anything else relating to dogs. There is a competition on the site in what photo gets most likes.

<br>

### **Site goal**
Site goal is to create a place where dog photos and only dog photos is found. This is to be like a safe haven for dog owners to interact with other dog owners and be able to discuss about the breed. Potentially, users can find from first-hand what certain breed is like.

<br>

### **Target audience**
For every dog lover on the planet. For anyone who would like to find out more about the breed from the owners of that breed. The ideal user age is between 20-60 years of age. 

<br>

### **User goals**
For dog owners to share their best friends with others, even just over the photo and for future dog owners to find out more about the breed they would like to own one day.

<br>

### **Future goals**
* Site to have a filter for users to easily find the breed they are looking for
* Competition to have a reward on weekly basis with a countdown timer
* Each user to have their own profile on the site
* Users to be able to follow other users and see their posted photos
* Ability to sign in with other social media accounts

<hr>

## **User stories**
Not all stories have been implemented. Some have been left for future implementations as the site grows and expands.


### **Admin stories**
**As an admin:**
1. I can **view and approve entries** so that **content submitted is appropriate** *(story points: 1)*


2. I can **approve comments** so that **the feedback provided is appropriate** *(story points: 1)*


3. I can **create a log in / sign up page** so that **users can sign up to the site** *(story points: 2)*


### **User stories**
**As a user:**
1. I can **easily see what photo has most likes** so that **I can see who is most likely to be a winner** *(story points: 2)*

2. I can **delete my entry** so that **I don't compete in the competition** *(story points: 1)*

3. I can **filter competition page** so that **I can see the photos uploaded in specific order** *(story points: 4)*

4. I can **see competitor's page** so that **I can see all the uploads by them** *(story points: 4)*

5. I can **follow the competitor** so that **I get updated when the submit new photo** *(story points: 4)*

6. I can **edit description I submitted with the photo** so that **I can add more information for others to see** *(story points: 2)*

7. I can **sign up with social media account** so **that sign in is quicker** *(story points: 2)*

8. I can **post comments on the photo** so that **I can tell what I think about the photo** *(story points: 4)*

9. I can **click on the photo** so that **I can see and read more about it** *(story points: 2)*

10. I can **view all entries** so that **I can see who entered the competition** *(story points: 1)*

11. I can **like photos** so that **the photo I liked gets more likes** *(story points: 2)*

12. I can **submit my dog photo** so that **I can be in the competition** *(story points: 2)*

<br>

## **Design**

### **Wireframe**

**Home page:**<br>
![Home page wireframe](static/images/readme-images/home-page-wireframe.png)

<br>

**Competition page:**<br>
![Competition page wireframe](static/images/readme-images/competition-page-wireframe.png)

<br>

**Entry detail page:**<br>
![Entry detail page wireframe](static/images/readme-images/entry-detail-page-wireframe.png)

<br>

**Site navigation:**<br>
![Site navigation](static/images/readme-images/site-navigation.png)


### **Database schema**<br>

### **Color palette**<br>
![Color palette](static/images/readme-images/color-palette.png)

### **Typography**
One font was used through the website. The font is from google fonts:
* Rowdies

### **Imagery**
* Header photo is from [Unsplash](https://unsplash.com/photos/U6nlG0Y5sfs) posted there by [Hannah Lim](https://unsplash.com/@hannah15198)
* Entry photos are from personal collection used for fictional users

<br>

## **Features**
<hr>

### **Existing features**

**Home Page**<br>
![Home page](static/images/readme-images/home-page.png)

<br>

**Navigation bar**<br>
*Desktop:*<br>
![Desktop navigation bar](static/images/readme-images/desktop-navbar.png)

<br>

*Mobile:*<br>
![Mobile navigation bar](static/images/readme-images/mobile-navbar.png)

<br>

**Rules Page**<br>
![Rules page](static/images/readme-images/rules-page.png)

<br>

**All Entries Page**<br>
![Rules page](static/images/readme-images/all-entries-page.png)

<br>

**Entry Detail Page**<br>
![Entry detail page](static/images/readme-images/entry-detail-page.png)

<br>

**Competition Page**<br>
![Competition Page](static/images/readme-images/competition-page.png)

<br>

**Sign up, Log in and Log out**

*Sign up*<br>
![Sign up page](static/images/readme-images/sign-up-page.png)

<br>

*Log in*<br>
![Log in page](static/images/readme-images/log-in-page.png)

<br>

*Log out*<br>
![Log out page](static/images/readme-images/log-out-page.png)

<br>

**Social Links**<br>
![Social Links](static/images/readme-images/social-links.png)

<br>

### **C.R.U.D.**<span id="crud"><span>
**Create (button)**<br>
* Enter button in navigation bar will bring user to a page with the form to submit their entry
* Enter button is only visible to users that are signed in

![Create for CRUD - button](static/images/readme-images/enter-button.png)

<br>

**Create (form)**<br>
* Form is only accessible through <button>Enter</button> button

![Create for CRUD - form](static/images/readme-images/enter-form.png)

<br>

**Read**<br>
![Read for CRUD](static/images/readme-images/all-entries-page.png)

<br>

**Update and delete**<br>
* The user who directly submitted the entry has an option to edit or delete their entry

![Update and delete for CRUD](static/images/readme-images/edit-delete-buttons.png)

<br>

### **Future features**
* Social media sign up
* Filter option in All Entries page
* Each user to have their own profile
* Possibility to follow other users

<hr>

## **Testing**
1. Navigation bar toggler button have additional border when clicked on:
* fixed by adding css style -> .navbar {--bs-navbar-color: #0d0058;}

<br>

2. Photos not showing on the All Entries page or entry_detail page:
* fixed:
    * misspelled "entry" in {{ entry.featured_image.url }} in All entries template <br>
    * forgot .url in {{ entry.featured_image.url }} in entry_detail page

<br>

3. Slug field not populating by itself when user makes a title input:
 * fixed by importing slugify from django.utils.text and adding "save" method inside class Enter - done as per instruction from StackOverflow (credited in Credits section) (credit to: stackoverflow - https://stackoverflow.com/questions/50436658/how-to-auto-generate-slug-from-my-album-model-in-django-2-0-4)

 <br>

4. White space on the right side of the website:
* fixed:
    * footer was missing a parent div with class "container" to div with class "row"

<br>

5. Image required test failed:
* fixed by changing error message from "This field is required." to "No file selected!" as per the error message in terminal

<br>

6. test_fields_are_explicit_in_form_metaclass faild:
 - fixed by changing the square brackets to parenthesies
