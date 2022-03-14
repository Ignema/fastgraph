-- CreateTable
CREATE TABLE "user" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL
);

-- CreateTable
CREATE TABLE "file" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "filename" TEXT NOT NULL,
    "extension" TEXT NOT NULL,
    "url" TEXT NOT NULL,
    "size" INTEGER,
    "created_date" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_date" DATETIME NOT NULL,
    "private" BOOLEAN NOT NULL,
    "access_token" TEXT,
    "user_id" INTEGER NOT NULL,
    CONSTRAINT "file_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "project" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "category" TEXT NOT NULL,
    "userId" INTEGER NOT NULL,
    "fileId" INTEGER NOT NULL,
    CONSTRAINT "project_userId_fkey" FOREIGN KEY ("userId") REFERENCES "user" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT "project_fileId_fkey" FOREIGN KEY ("fileId") REFERENCES "file" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "image" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "height" INTEGER,
    "width" INTEGER,
    "projectId" INTEGER NOT NULL,
    "fileId" INTEGER NOT NULL,
    CONSTRAINT "image_fileId_fkey" FOREIGN KEY ("fileId") REFERENCES "file" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT "image_projectId_fkey" FOREIGN KEY ("projectId") REFERENCES "project" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "presentation" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" TEXT NOT NULL,
    "total_slides" INTEGER,
    "fileId" INTEGER NOT NULL,
    CONSTRAINT "presentation_fileId_fkey" FOREIGN KEY ("fileId") REFERENCES "file" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "document" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "font" TEXT NOT NULL,
    "text_size" INTEGER NOT NULL,
    "characters" INTEGER,
    "fileId" INTEGER NOT NULL,
    CONSTRAINT "document_fileId_fkey" FOREIGN KEY ("fileId") REFERENCES "file" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "audio" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "length" INTEGER,
    "fileId" INTEGER NOT NULL,
    CONSTRAINT "audio_fileId_fkey" FOREIGN KEY ("fileId") REFERENCES "file" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "music" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "author" TEXT NOT NULL,
    "album" TEXT NOT NULL,
    "genre" TEXT NOT NULL,
    "audioId" INTEGER NOT NULL,
    CONSTRAINT "music_audioId_fkey" FOREIGN KEY ("audioId") REFERENCES "audio" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "video" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "height" INTEGER,
    "width" INTEGER,
    "length" INTEGER,
    "genre" TEXT NOT NULL,
    "season" INTEGER NOT NULL,
    "title" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "fileId" INTEGER NOT NULL,
    CONSTRAINT "video_fileId_fkey" FOREIGN KEY ("fileId") REFERENCES "file" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "thumbnail" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "videoId" INTEGER NOT NULL,
    "imageId" INTEGER NOT NULL,
    CONSTRAINT "thumbnail_imageId_fkey" FOREIGN KEY ("imageId") REFERENCES "image" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT "thumbnail_videoId_fkey" FOREIGN KEY ("videoId") REFERENCES "video" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateIndex
CREATE UNIQUE INDEX "user_email_key" ON "user"("email");

-- CreateIndex
CREATE UNIQUE INDEX "filename_size_unique" ON "file"("filename", "size");

-- CreateIndex
CREATE UNIQUE INDEX "project_name_key" ON "project"("name");

-- CreateIndex
CREATE UNIQUE INDEX "project_fileId_key" ON "project"("fileId");

-- CreateIndex
CREATE UNIQUE INDEX "image_fileId_key" ON "image"("fileId");

-- CreateIndex
CREATE UNIQUE INDEX "presentation_title_key" ON "presentation"("title");

-- CreateIndex
CREATE UNIQUE INDEX "presentation_fileId_key" ON "presentation"("fileId");

-- CreateIndex
CREATE UNIQUE INDEX "document_fileId_key" ON "document"("fileId");

-- CreateIndex
CREATE UNIQUE INDEX "audio_fileId_key" ON "audio"("fileId");

-- CreateIndex
CREATE UNIQUE INDEX "music_audioId_key" ON "music"("audioId");

-- CreateIndex
CREATE UNIQUE INDEX "video_title_key" ON "video"("title");

-- CreateIndex
CREATE UNIQUE INDEX "video_fileId_key" ON "video"("fileId");

-- CreateIndex
CREATE UNIQUE INDEX "thumbnail_videoId_key" ON "thumbnail"("videoId");

-- CreateIndex
CREATE UNIQUE INDEX "thumbnail_imageId_key" ON "thumbnail"("imageId");
