<template>
    <div>
        <b-navbar toggleable="lg" type="dark"  variant="dark">
            <a class="navbar-brand " href='/'>
                <img src="../../public/favicon.png" width="35" height="35" class="d-inline-block align-top" alt="penguin">
                acsys</a>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav class="mr-auto">
                    <b-nav-item href="/updateinformation">更新情報</b-nav-item>
                </b-navbar-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item href="/login">ログイン</b-nav-item>
                    <b-nav-item href="/signup">新規登録</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>