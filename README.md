<big><pre>
📂 [public](./public) # Supplemental assets or resources, or static files
📂 [src](./src) # Source files
├── 📂 [components](./src/components) 
│   ├── 📂 [reusable](./src/components/reusable) 
├── 📂 [images](./src/images) 
├── 📂 [tree](./src/tree) 
├── 📂 [utils](./src/utils) 
</pre></big>

<big><pre>
📜 [.eslintrc.js](./.eslintrc.js) 
📄 [.gitignore](./.gitignore) 
📂 [LICENSE](./LICENSE) 
📄 [README.md](./README.md) 
📄 [package-lock.json](./package-lock.json) 
📄 [package.json](./package.json) 
📂 [public](./public)            # Supplemental assets or resources, or static files
├── 📄 [favicon.ico](./public/favicon.ico) 
├── 📄 [index.html](./public/index.html) 
📂 [src](./src)               # Source files
├── 📄 [App.tsx](./src/App.tsx) 
├── 📂 [components](./src/components) 
│   ├── 📄 [BadgesSection.tsx](./src/components/BadgesSection.tsx) 
│   ├── 📄 [MarkdownDisplay.tsx](./src/components/MarkdownDisplay.tsx) 
│   ├── 📄 [MarkdownDisplayLine.tsx](./src/components/MarkdownDisplayLine.tsx) 
│   ├── 📄 [URLBox.tsx](./src/components/URLBox.tsx) 
│   ├── 📂 [reusable](./src/components/reusable) 
│   │   ├── 📄 [Card.tsx](./src/components/reusable/Card.tsx) 
│   │   ├── 📄 [CenteredCol.tsx](./src/components/reusable/CenteredCol.tsx) 
│   │   ├── 📄 [CustomButton.tsx](./src/components/reusable/CustomButton.tsx) 
│   │   ├── 📄 [CustomSecondaryButton.tsx](./src/components/reusable/CustomSecondaryButton.tsx) 
│   │   ├── 📄 [Input.tsx](./src/components/reusable/Input.tsx) 
├── 📂 [images](./src/images) 
│   ├── 📄 [Demo.gif](./src/images/Demo.gif) 
├── 📄 [index.css](./src/index.css) 
├── 📄 [index.tsx](./src/index.tsx) 
├── 📜 [react-app-env.d.ts](./src/react-app-env.d.ts) 
├── 📂 [tree](./src/tree) 
│   ├── 📄 [constants.ts](./src/tree/constants.ts) 
│   ├── 📄 [index.ts](./src/tree/index.ts) 
│   ├── 📄 [types.ts](./src/tree/types.ts) 
├── 📂 [utils](./src/utils) 
│   ├── 📄 [SelectRootCoresTest.ts](./src/utils/SelectRootCoresTest.ts) 
│   ├── 📄 [Switch.tsx](./src/utils/Switch.tsx) 
│   ├── 📄 [deleteFileFromPath.ts](./src/utils/deleteFileFromPath.ts) 
│   ├── 📄 [deleteFileFromPathTest.ts](./src/utils/deleteFileFromPathTest.ts) 
│   ├── 📄 [filterChange.ts](./src/utils/filterChange.ts) 
│   ├── 📄 [generateMarkDownTree.ts](./src/utils/generateMarkDownTree.ts) 
│   ├── 📄 [generateMarkDownTreeTest.ts](./src/utils/generateMarkDownTreeTest.ts) 
│   ├── 📄 [getAutoGeneratedCommentForPath.ts](./src/utils/getAutoGeneratedCommentForPath.ts) 
│   ├── 📄 [getAutoGeneratedCommentForPathtest.ts](./src/utils/getAutoGeneratedCommentForPathtest.ts) 
│   ├── 📄 [getCopyToClipboardContents.ts](./src/utils/getCopyToClipboardContents.ts) 
│   ├── 📄 [getCopyToClipboardContentsTest.ts](./src/utils/getCopyToClipboardContentsTest.ts) 
│   ├── 📄 [getFileIconFromFileType.ts](./src/utils/getFileIconFromFileType.ts) 
│   ├── 📄 [getFileIconFromFileTypeTest.ts](./src/utils/getFileIconFromFileTypeTest.ts) 
│   ├── 📄 [getFileTypeFromPath.ts](./src/utils/getFileTypeFromPath.ts) 
│   ├── 📄 [getFileTypeFromPathTest.ts](./src/utils/getFileTypeFromPathTest.ts) 
│   ├── 📄 [getHyperLinkFromPath.ts](./src/utils/getHyperLinkFromPath.ts) 
│   ├── 📄 [getHyperLinkFromPathtest.ts](./src/utils/getHyperLinkFromPathtest.ts) 
│   ├── 📄 [getLargestFileNameLengthInLevel.ts](./src/utils/getLargestFileNameLengthInLevel.ts) 
│   ├── 📄 [getLargestFileNameLengthInLevelTest.ts](./src/utils/getLargestFileNameLengthInLevelTest.ts) 
│   ├── 📄 [repoToBadge.ts](./src/utils/repoToBadge.ts) 
│   ├── 📄 [selectFoldersOnly.ts](./src/utils/selectFoldersOnly.ts) 
│   ├── 📄 [selectFoldersOnlyTest.ts](./src/utils/selectFoldersOnlyTest.ts) 
│   ├── 📄 [selectRootCores.ts](./src/utils/selectRootCores.ts) 
│   ├── 📄 [setCommentForPath.ts](./src/utils/setCommentForPath.ts) 
│   ├── 📄 [setCommentForPathtest.ts](./src/utils/setCommentForPathtest.ts) 
│   ├── 📄 [undoDeletions.ts](./src/utils/undoDeletions.ts) 
│   ├── 📄 [undoDeletionsTest.ts](./src/utils/undoDeletionsTest.ts) 
📄 [tsconfig.json](./tsconfig.json) 
</pre></big>

# List-Maker
This is a python program I wrote
After choosing a folder, the program makes a txt file which includes all the subfolders and files inside them
