
# On-Licence Housing Allocation System - Wireframes

This document describes the wireframes for the On-Licence Housing Allocation System.

## 1. Login Screen

*   **Title:** Welcome to the Housing Allocation System
*   **Fields:**
    *   Username (text input)
    *   Password (password input)
*   **Buttons:**
    *   Login
    *   Register
*   **Link:** Forgot Password

## 2. Registration Screen (for Applicants)

*   **Title:** Create Your Account
*   **Fields:**
    *   Full Name (text input)
    *   Date of Birth (date picker)
    *   Email Address (email input)
    *   Phone Number (text input)
    *   Username (text input)
    *   Password (password input)
    *   Confirm Password (password input)
*   **Button:** Register

## 3. Applicant Dashboard

*   **Header:** Welcome, [Applicant Name]!
*   **Section: Application Status**
    *   Displays the current status of the application (e.g., "Not Started", "In Progress", "Submitted", "Under Review", "Approved", "Rejected").
*   **Section: My Application**
    *   Button: "Start New Application" (if no application exists)
    *   Button: "Continue Application" (if an application is in progress)
    *   Button: "View Application" (if an application has been submitted)
*   **Section: My Profile**
    *   Button: "Edit Profile"
*   **Section: Available Properties**
    *   A search bar to search for properties by location or keyword.
    *   Filter options (e.g., number of bedrooms, rent range).
    *   A list of properties with a brief summary (photo, address, rent, bedrooms).
*   **Footer:**
    *   Logout Button

## 4. Housing Application Form

*   **Title:** Housing Application
*   **Multi-step form with a progress bar at the top.**

    *   **Step 1: Personal Details**
        *   Fields for name, DOB, contact information, etc.
    *   **Step 2: Household Composition**
        *   A table to add details of all household members.
    *   **Step 3: Financial Information**
        *   Fields for income, employment details, and benefits.
    *   **Step 4: Housing History**
        *   Fields for previous addresses and landlord details.
    *   **Step 5: Supporting Documents**
        *   File upload controls for documents like ID, proof of income, etc.

*   **Buttons on each step:**
    *   Save and Continue
    *   Back
*   **Button on the final step:**
    *   Submit Application

## 5. Housing Officer Dashboard

*   **Header:** Housing Officer Dashboard
*   **Section: Pending Applications**
    *   A table of pending applications with columns for:
        *   Applicant Name
        *   Application ID
        *   Submission Date
        *   Status
*   **Search and Filter:**
    *   Search bar for applications.
    *   Filter options by status, date, etc.
*   **Section: My Tasks**
    *   A list of assigned tasks (e.g., "Review Application X", "Follow up with Applicant Y").
*   **Footer:**
    *   Logout Button

## 6. Application Review Screen (for Housing Officers)

*   **Title:** Application Review - [Applicant Name]
*   **Tabs for each section of the application:**
    *   Personal Details
    *   Household Composition
    *   Financial Information
    *   Housing History
    *   Supporting Documents
*   **Section: Supporting Documents**
    *   A list of uploaded documents with links to view or download them.
*   **Section: Notes & Comments**
    *   A text area for the officer to add notes.
*   **Action Buttons:**
    *   Approve
    *   Reject
    *   Request More Information

## 7. Property Listing Screen (for Applicants)

*   **Title:** Available Properties
*   **View Options:**
    *   Grid View
    *   List View
*   **Property Card (for each property):**
    *   Image of the property
    *   Address
    *   Rent per month
    *   Number of bedrooms
    *   A "View Details" button

## 8. Property Details Screen (for Applicants)

*   **Title:** [Property Address]
*   **Image Gallery:** Multiple photos of the property.
*   **Details Section:**
    *   Full description of the property.
    *   Key features (e.g., parking, garden).
    *   Map showing the location.
*   **Action Button:**
    *   Apply Now (if the applicant is eligible)
